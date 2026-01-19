# Rubber Robot State Machine Diagram

## Main State Machine (`rubber_state_machine`)

```mermaid
stateDiagram-v2
    [*] --> IDLE
    
    IDLE --> DETECT_PAD_PICK_STATE: Start cycle
    DETECT_PAD_PICK_STATE --> PRESSING_ARM_DOWN_STATE: Pad pick detected
    PRESSING_ARM_DOWN_STATE --> MOVE_TO_PRODUCT_SCAN_POSITION: Arm down complete
    MOVE_TO_PRODUCT_SCAN_POSITION --> SCAN_PRODUCT_STATE: At scan position
    SCAN_PRODUCT_STATE --> DETECT_PAD_PLACE_STATE: Scan complete
    DETECT_PAD_PLACE_STATE --> PAD_ATTACH_STATE: Pad positions detected / retry
    PAD_ATTACH_STATE --> PAD_ATTACH_STATE: Loop (nested state machine)
    PAD_ATTACH_STATE --> PAD_VALIDATION_STATE: All pads attached
    PAD_VALIDATION_STATE --> SCOOP_PAD_STATE: Pad loosen enabled
    PAD_VALIDATION_STATE --> MOVE_HOME_STATE: Pad loosen disabled
    SCOOP_PAD_STATE --> COMPLETED_STATE: Scoop complete
    MOVE_HOME_STATE --> PRESSING_ARM_UP_STATE: At home
    PRESSING_ARM_UP_STATE --> COMPLETED_STATE: Arm up complete
    COMPLETED_STATE --> [*]: Cycle complete
    
    DETECT_PAD_PLACE_STATE --> DETECT_PAD_PLACE_STATE: Retry (up to 4x)
    DETECT_PAD_PLACE_STATE --> COMPLETED_STATE: Detection failed (4 retries)
    PAD_ATTACH_STATE --> ERROR_STATE: Detection check failed
    MOVE_TO_PRODUCT_SCAN_POSITION --> ERROR_STATE: Pressing arm ACK not received
    
    any_state --> ERROR_STATE: Error condition
    ERROR_STATE --> [*]: Error handled
```

## Pad Execution State Machine (`pad_execution_state`)

```mermaid
stateDiagram-v2
    [*] --> IDLE
    
    IDLE --> PICK_PAD_STATE: Start pad attach
    PICK_PAD_STATE --> ERROR_STATE: No pad exists
    PICK_PAD_STATE --> PLACE_PAD_STATE: Pad picked successfully
    PLACE_PAD_STATE --> IDLE: More pads remaining (rescan)
    PLACE_PAD_STATE --> IDLE: More pads remaining (no rescan)
    PLACE_PAD_STATE --> COMPLETED_STATE: All pads placed
    COMPLETED_STATE --> IDLE: Reset for next cycle
    COMPLETED_STATE --> PAD_VALIDATION_STATE: Exit to main state machine
    
    RETRY_PAD_PICK_STATE --> PICK_PAD_STATE: Retry pick
    ERROR_STATE --> IDLE: Error handled
    
    any_state --> ERROR_STATE: Error condition
```

## Combined Flow Diagram

```mermaid
graph TB
    subgraph "Main State Machine"
        A[IDLE] --> B[DETECT_PAD_PICK]
        B --> C[PRESSING_ARM_DOWN]
        C --> D[MOVE_TO_SCAN]
        D --> E[SCAN_PRODUCT]
        E --> F[DETECT_PAD_PLACE]
        F --> G[PAD_ATTACH]
        G --> H[PAD_VALIDATION]
        H --> I{MOVE_HOME or SCOOP}
        I --> J[PRESSING_ARM_UP]
        J --> K[COMPLETED]
        K --> L[END]
    end
    
    subgraph "Pad Execution State Machine (Nested)"
        G1[IDLE] --> G2[PICK_PAD]
        G2 --> G3[PLACE_PAD]
        G3 --> G4{More Pads?}
        G4 -->|Yes| G1
        G4 -->|No| G5[COMPLETED]
        G5 --> G1
        G5 --> H
    end
    
    G -.contains.-> G1
    
    style K fill:#90EE90
    style L fill:#FFB6C1
    style G5 fill:#90EE90
    style ERROR fill:#FF6B6B
```

## Pad Execution State Machine Detailed Flowchart with Bug Locations

```mermaid
flowchart TD
    Start([Pad Execution State Machine Starts]) --> CheckIDLE{Current State = IDLE?}
    
    CheckIDLE -->|Yes| IDLE_Logic[IDLE State Logic]
    IDLE_Logic --> ToPick[MOVING_TO_PICK_PAD_STATE<br/>Actually transitions to PICK_PAD_STATE]
    
    CheckIDLE -->|No| CheckPick{State = PICK_PAD_STATE?}
    CheckPick -->|Yes| PickLogic[Pick pad from paper]
    PickLogic --> CheckPadExists{Pad exists?}
    CheckPadExists -->|No| ToError[ERROR_STATE]
    CheckPadExists -->|Yes| ToPlace[PLACE_PAD_STATE]
    
    CheckIDLE -->|No| CheckPlace{State = PLACE_PAD_STATE?}
    CheckPlace -->|Yes| PlaceLogic[Place pad on product]
    PlaceLogic --> IncrementCount[Increment repeat_count]
    IncrementCount --> MorePads{More pads?}
    MorePads -->|Yes| CheckRescan{Rescan enabled?}
    MorePads -->|No| ToCompleted[COMPLETED_STATE]
    
    CheckRescan -->|Yes| RescanLogic[Transition to IDLE<br/>AND transition main state<br/>to MOVE_TO_PRODUCT_SCAN_POSITION]
    CheckRescan -->|No| BackToIDLE[Transition to IDLE]
    RescanLogic --> Bug6[🐛 BUG #6: Double transition<br/>Execution: PLACE_PAD → IDLE<br/>Main: PAD_ATTACH → MOVE_TO_SCAN<br/>Location: Lines 684-687]
    Bug6 --> BackToIDLE
    
    ToCompleted --> Bug2[🐛 BUG #2: Double Transition<br/>1. Execution: COMPLETED → IDLE<br/>2. Main: PAD_ATTACH → PAD_VALIDATION<br/>Location: Lines 695-701]
    Bug2 --> MainTransition[Transition main state machine]
    MainTransition --> Bug3[🐛 BUG #3: Re-entry Risk<br/>Main state may still be PAD_ATTACH_STATE<br/>when execution state becomes IDLE<br/>Location: Line 95-152]
    Bug3 --> End([End])
    
    CheckIDLE -->|No| CheckCompleted{State = COMPLETED_STATE?}
    CheckCompleted -->|Yes| Bug2
    
    CheckIDLE -->|No| CheckError{State = ERROR_STATE?}
    CheckError -->|Yes| ErrorLogic[ERROR_STATE Logic]
    ErrorLogic --> Bug4[🐛 BUG #4: Transitions back to IDLE<br/>but main state still PAD_ATTACH_STATE<br/>Location: Lines 710-728]
    Bug4 --> BackToIDLE
    
    CheckIDLE -->|No| CheckRetry{State = RETRY_PAD_PICK_STATE?}
    CheckRetry -->|Yes| RetryLogic[Retry picking pad]
    RetryLogic --> ToPick
    
    style Bug2 fill:#FF6B6B,stroke:#000,stroke-width:3px
    style Bug3 fill:#FF6B6B,stroke:#000,stroke-width:3px
    style Bug4 fill:#FFA500,stroke:#000,stroke-width:2px
    style Bug6 fill:#FFA500,stroke:#000,stroke-width:2px
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
    CheckState -->|DETECT_PAD_PICK| DetectPick[DETECT_PAD_PICK_STATE]
    CheckState -->|PRESSING_ARM_DOWN| PressDown[PRESSING_ARM_DOWN_STATE]
    CheckState -->|MOVE_TO_SCAN| MoveScan[MOVE_TO_PRODUCT_SCAN_POSITION]
    CheckState -->|SCAN| Scan[SCAN_PRODUCT_STATE]
    CheckState -->|DETECT_PAD_PLACE| DetectPlace[DETECT_PAD_PLACE_STATE]
    CheckState -->|PAD_ATTACH| Bug1[🐛 BUG #1: Conditional state_cmd_executing flag<br/>Line 95-152: Only set in retry/error paths<br/>NOT set in normal execution path!]
    CheckState -->|PAD_VALIDATION| Validation[PAD_VALIDATION_STATE]
    CheckState -->|MOVE_HOME| MoveHome[MOVE_HOME_STATE]
    CheckState -->|SCOOP_PAD| Scoop[SCOOP_PAD_STATE]
    CheckState -->|PRESSING_ARM_UP| PressUp[PRESSING_ARM_UP_STATE]
    CheckState -->|COMPLETED| Complete[COMPLETED_STATE]
    CheckState -->|ERROR| Error[ERROR_STATE]
    
    Bug1 --> CheckRetry{Retry needed?}
    CheckRetry -->|Yes| SetFlag1[state_cmd_executing = true<br/>✅ Flag set]
    CheckRetry -->|No| CheckFail{Failed 4 times?}
    CheckFail -->|Yes| SetFlag2[state_cmd_executing = true<br/>✅ Flag set]
    CheckFail -->|No| Bug1Risk[🐛 BUG #1: Normal path<br/>state_cmd_executing NOT set!<br/>⚠️ Allows re-entry]
    
    SetFlag1 --> CallExecution[Call pad_execution_state]
    SetFlag2 --> CallExecution
    Bug1Risk --> CallExecution
    
    CallExecution --> ExecutionRunning[Execution State Machine Running]
    ExecutionRunning --> Bug3Risk[🐛 BUG #3 Risk: If execution completes<br/>and transitions states, main state<br/>may still be PAD_ATTACH_STATE<br/>causing re-entry]
    Bug3Risk --> EndMain
    
    IDLE_Main --> NextState[Transition to next state]
    DetectPick --> NextState
    PressDown --> NextState
    MoveScan --> NextState
    Scan --> NextState
    DetectPlace --> NextState
    Validation --> NextState
    MoveHome --> NextState
    Scoop --> NextState
    PressUp --> NextState
    Complete --> EndMain
    Error --> EndMain
    
    NextState --> CheckActive
    
    style Bug1 fill:#FF6B6B,stroke:#000,stroke-width:3px
    style Bug1Risk fill:#FF6B6B,stroke:#000,stroke-width:3px
    style Bug3Risk fill:#FF6B6B,stroke:#000,stroke-width:3px
    style CallExecution fill:#FFA500,stroke:#000,stroke-width:2px
    style EndMain fill:#FFB6C1
```

