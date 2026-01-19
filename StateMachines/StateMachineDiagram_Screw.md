# Screw Robot State Machine Diagram

## Main State Machine (`screw_state_machine`)

```mermaid
stateDiagram-v2
    [*] --> IDLE
    
    IDLE --> PRESSING_ARM_DOWN_STATE: Start cycle
    PRESSING_ARM_DOWN_STATE --> MOVE_TO_PRODUCT_SCAN_POSITION: Arm down complete
    MOVE_TO_PRODUCT_SCAN_POSITION --> SCAN_PRODUCT_STATE: At scan position
    SCAN_PRODUCT_STATE --> DETECT_HOLE_POSITIONS_STATE: Scan complete
    DETECT_HOLE_POSITIONS_STATE --> SCREWING_EXECUTION_STATE: Holes detected / disabled
    SCREWING_EXECUTION_STATE --> SCREWING_EXECUTION_STATE: Loop (nested state machine)
    SCREWING_EXECUTION_STATE --> MOVING_TO_RETRACT_POSITION: All screws done
    MOVING_TO_RETRACT_POSITION --> PRESSING_ARM_UP_STATE: At retract position
    PRESSING_ARM_UP_STATE --> COMPLETED_STATE: Arm up complete
    COMPLETED_STATE --> [*]: Cycle complete
    
    DETECT_HOLE_POSITIONS_STATE --> SCREWING_EXECUTION_STATE: Retry (up to 4x)
    SCREWING_EXECUTION_STATE --> COMPLETED_STATE: Hole detection failed (4 retries)
    
    any_state --> ERROR_STATE: Error condition
    ERROR_STATE --> [*]: Error handled
```

## Screw Execution State Machine (`screw_execution_state`)

```mermaid
stateDiagram-v2
    [*] --> IDLE
    
    IDLE --> MOVING_TO_SCREW_PICK_POSITION: Screw needed & not on bit
    IDLE --> MOVING_TO_FASTENING_POSITION: Screw already on bit
    IDLE --> DETECT_HOLE_POSITIONS_STATE: Retry hole detection (if empty, < 4 retries)
    IDLE --> COMPLETED_STATE: All screws done OR hole detection failed (4 retries)
    
    MOVING_TO_SCREW_PICK_POSITION --> SCREW_DROP_STATE: Timeout detected
    MOVING_TO_SCREW_PICK_POSITION --> SCREW_PICK_STATE: At feeder ready position
    
    SCREW_PICK_STATE --> CHECK_SCREW_PICK_STATE: Pick complete
    CHECK_SCREW_PICK_STATE --> MOVING_TO_FASTENING_POSITION: Validation passed / disabled
    CHECK_SCREW_PICK_STATE --> COMPLETED_STATE: Validation failed (timeout)
    
    MOVING_TO_FASTENING_POSITION --> SCREW_FASTENING_STATE: At fastening position
    SCREW_FASTENING_STATE --> SCREW_CHECK_STATE: More screws remaining
    SCREW_FASTENING_STATE --> COMPLETED_STATE: All screws done
    
    SCREW_CHECK_STATE --> IDLE: Rescan enabled
    SCREW_CHECK_STATE --> IDLE: Rescan disabled
    
    SCREW_DROP_STATE --> MOVING_TO_PRE_PICK_SCREW: Drop complete
    MOVING_TO_PRE_PICK_SCREW --> SCREW_PICK_STATE: At feeder ready position
    
    COMPLETED_STATE --> IDLE: Reset for next cycle
    COMPLETED_STATE --> MOVING_TO_RETRACT_POSITION: Exit to main state machine
    
    any_state --> ERROR_STATE: Error condition
```

## Combined Flow Diagram

```mermaid
graph TB
    subgraph "Main State Machine"
        A[IDLE] --> B[PRESSING_ARM_DOWN]
        B --> C[MOVE_TO_SCAN]
        C --> D[SCAN_PRODUCT]
        D --> E[DETECT_HOLES]
        E --> F[SCREWING_EXECUTION]
        F --> G[MOVING_TO_RETRACT]
        G --> H[PRESSING_ARM_UP]
        H --> I[COMPLETED]
        I --> J[END]
    end
    
    subgraph "Screw Execution State Machine (Nested)"
        F1[IDLE] --> F2{Need Screw?}
        F2 -->|Yes| F3[MOVING_TO_PICK]
        F2 -->|No| F7[MOVING_TO_FASTEN]
        F3 --> F4[SCREW_PICK]
        F4 --> F5[CHECK_PICK]
        F5 --> F7
        F7 --> F8[SCREW_FASTENING]
        F8 --> F9{More Screws?}
        F9 -->|Yes| F10[SCREW_CHECK]
        F9 -->|No| F11[COMPLETED]
        F10 --> F1
        F11 --> F1
        F11 --> G
    end
    
    F -.contains.-> F1
    
    style I fill:#90EE90
    style J fill:#FFB6C1
    style F11 fill:#90EE90
    style ERROR fill:#FF6B6B
```

## Potential Issues Identified

### 🔴 Issue 1: Missing `state_cmd_executing` flag in SCREWING_EXECUTION_STATE
**Location:** Line 103
```cpp
// state_cmd_executing.store(true);  // COMMENTED OUT!
```
**Problem:** The main state machine's `SCREWING_EXECUTION_STATE` doesn't set the execution flag, which could cause race conditions or allow the state to be re-entered incorrectly.

### 🔴 Issue 2: COMPLETED_STATE transition logic
**Location:** Lines 628-634
**Problem:** The `COMPLETED_STATE` in the execution state machine:
1. Transitions back to `IDLE` 
2. Then transitions the main state machine to `MOVING_TO_RETRACT_POSITION`

This double transition could cause issues if the state machine is checked between these two commands.

### 🔴 Issue 3: Hole detection retry logic
**Location:** Lines 300-328
**Problem:** When hole detection fails, it transitions back to `DETECT_HOLE_POSITIONS_STATE` in the main state machine, but the execution state machine's `IDLE` state is still active. This could cause state confusion.

### 🔴 Issue 4: SCREW_CHECK_STATE transition
**Location:** Lines 598-626
**Problem:** `SCREW_CHECK_STATE` always transitions to `IDLE` regardless of whether rescan is enabled or not. If rescan is enabled, it also triggers hole detection which might transition the main state machine, causing potential conflicts.

### 🔴 Issue 5: No explicit ERROR_STATE handling in execution state machine
**Location:** Throughout `screw_execution_state()`
**Problem:** While `ERROR_STATE` exists in the enum, there's no explicit handling for it in the execution state machine, only a catch-all `else` clause that logs "unknown state".

## Execution State Machine Detailed Flowchart with Bug Locations

```mermaid
flowchart TD
    Start([Execution State Machine Starts]) --> CheckIDLE{Current State = IDLE?}
    
    CheckIDLE -->|Yes| IDLE_Logic[IDLE State Logic]
    IDLE_Logic --> CheckEmpty{Hole positions empty?}
    CheckEmpty -->|Yes| CheckRetry{Retry count < 4?}
    CheckRetry -->|Yes| RetryHoleDetection[Move to retry position<br/>Transition to DETECT_HOLE_POSITIONS_STATE]
    CheckRetry -->|No| FailToMain[Transition to COMPLETED_STATE<br/>Main state: COMPLETED_STATE]
    CheckEmpty -->|No| CheckScrewOnBit{Screw on bit?}
    CheckScrewOnBit -->|No| ToPick[MOVING_TO_SCREW_PICK_POSITION]
    CheckScrewOnBit -->|Yes| ToFasten[MOVING_TO_FASTENING_POSITION]
    
    CheckIDLE -->|No| CheckMovingPick{State = MOVING_TO_SCREW_PICK_POSITION?}
    CheckMovingPick -->|Yes| CheckTimeout{Timeout detected?}
    CheckTimeout -->|Yes| ToDrop[SCREW_DROP_STATE]
    CheckTimeout -->|No| ToPickState[SCREW_PICK_STATE]
    
    ToPickState --> PickLogic[Pick screw from feeder]
    PickLogic --> CheckPick[CHECK_SCREW_PICK_STATE]
    CheckPick --> ValidationEnabled{Validation enabled?}
    ValidationEnabled -->|Yes| WaitValidation[Wait for validation result]
    ValidationEnabled -->|No| ToFasten
    
    ToFasten --> FastenLogic[MOVING_TO_FASTENING_POSITION]
    FastenLogic --> Fastening[SCREW_FASTENING_STATE]
    Fastening --> IncrementCount[Increment repeat_count]
    IncrementCount --> MoreScrews{More screws?}
    MoreScrews -->|Yes| CheckRescan{Rescan enabled?}
    MoreScrews -->|No| ToCompleted[COMPLETED_STATE]
    
    CheckRescan -->|Yes| RescanLogic[SCREW_CHECK_STATE<br/>Move to scan position<br/>Detect holes again]
    CheckRescan -->|No| BackToIDLE[Transition to IDLE]
    RescanLogic --> BackToIDLE
    
    ToCompleted --> Bug2[🐛 BUG #2: Double Transition<br/>1. Execution: COMPLETED → IDLE<br/>2. Main: SCREWING_EXECUTION → MOVING_TO_RETRACT<br/>Location: Lines 628-634]
    Bug2 --> MainTransition[Transition main state machine]
    MainTransition --> Bug3[🐛 BUG #3: Re-entry Risk<br/>Main state may still be SCREWING_EXECUTION_STATE<br/>when execution state becomes IDLE<br/>Location: Line 101-103]
    Bug3 --> End([End])
    
    ToDrop --> DropLogic[Drop screw at feeder]
    DropLogic --> PrePick[MOVING_TO_PRE_PICK_SCREW]
    PrePick --> ToPickState
    
    CheckIDLE -->|No| CheckCompleted{State = COMPLETED_STATE?}
    CheckCompleted -->|Yes| Bug2
    
    CheckIDLE -->|No| CheckDrop{State = SCREW_DROP_STATE?}
    CheckDrop -->|Yes| ToDrop
    
    CheckIDLE -->|No| CheckError{State = ERROR_STATE?}
    CheckError -->|Yes| Bug5[🐛 BUG #5: No explicit handling<br/>Only catch-all else clause<br/>Location: Line 669]
    Bug5 --> End
    
    style Bug2 fill:#FF6B6B,stroke:#000,stroke-width:3px
    style Bug3 fill:#FF6B6B,stroke:#000,stroke-width:3px
    style Bug5 fill:#FFA500,stroke:#000,stroke-width:2px
    style ToCompleted fill:#90EE90
    style End fill:#FFB6C1
```

## Main State Machine Entry Point with Bug Location

```mermaid
flowchart TD
    MainStart([Main State Machine Loop]) --> CheckActive{FSM_PROCESS_ACTIVE<br/>&&<br/>!fsm_process_is_paused?}
    CheckActive -->|No| EndMain([End])
    CheckActive -->|Yes| CheckState{Current System State?}
    
    CheckState -->|IDLE| IDLE_Main[IDLE State]
    CheckState -->|PRESSING_ARM_DOWN| PressDown[PRESSING_ARM_DOWN_STATE]
    CheckState -->|MOVE_TO_SCAN| MoveScan[MOVE_TO_PRODUCT_SCAN_POSITION]
    CheckState -->|SCAN| Scan[SCAN_PRODUCT_STATE]
    CheckState -->|DETECT_HOLES| Detect[DETECT_HOLE_POSITIONS_STATE]
    CheckState -->|SCREWING_EXECUTION| Bug1[🐛 BUG #1: Missing state_cmd_executing flag<br/>Line 103: Commented out!<br/>Allows re-entry of execution state machine]
    CheckState -->|MOVING_TO_RETRACT| MoveRetract[MOVING_TO_RETRACT_POSITION]
    CheckState -->|PRESSING_ARM_UP| PressUp[PRESSING_ARM_UP_STATE]
    CheckState -->|COMPLETED| Complete[COMPLETED_STATE]
    CheckState -->|ERROR| Error[ERROR_STATE]
    
    Bug1 --> CheckExecFlag{!state_cmd_executing?}
    CheckExecFlag -->|Yes| CallExecution[Call screw_execution_state<br/>⚠️ WITHOUT setting flag!]
    CheckExecFlag -->|No| Skip[Skip - already executing]
    
    CallExecution --> ExecutionRunning[Execution State Machine Running]
    ExecutionRunning --> Bug3Risk[🐛 BUG #3 Risk: If execution completes<br/>and transitions states, main state<br/>may still be SCREWING_EXECUTION_STATE<br/>causing re-entry]
    Bug3Risk --> EndMain
    
    IDLE_Main --> NextState[Transition to next state]
    PressDown --> NextState
    MoveScan --> NextState
    Scan --> NextState
    Detect --> NextState
    MoveRetract --> NextState
    PressUp --> NextState
    Complete --> EndMain
    Error --> EndMain
    
    NextState --> CheckActive
    
    style Bug1 fill:#FF6B6B,stroke:#000,stroke-width:3px
    style Bug3Risk fill:#FF6B6B,stroke:#000,stroke-width:3px
    style CallExecution fill:#FFA500,stroke:#000,stroke-width:2px
    style EndMain fill:#FFB6C1
```

## Recommended Fixes

1. **Uncomment the `state_cmd_executing` flag** in `SCREWING_EXECUTION_STATE`
2. **Review COMPLETED_STATE transitions** - ensure atomic state transitions
3. **Add explicit ERROR_STATE handling** in the execution state machine
4. **Clarify SCREW_CHECK_STATE logic** - ensure proper state synchronization
5. **Add state validation** before transitions to prevent invalid state combinations

