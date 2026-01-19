# Full Log Issues: Visual Analysis

## Critical Bug Timeline

```mermaid
gantt
    title Critical Issues Timeline
    dateFormat HH:mm:ss
    axisFormat %H:%M:%S
    
    section Normal Operations
    DETECT_HOLES (1st cycle)     :done, dh1, 23:06:17, 4s
    Vision wait                  :active, vw1, 23:06:18, 7s
    
    section Issue #1: Conveyor Timeout
    Conveyor timeout #1          :crit, ct1, 23:06:21, 1s
    Clean up #1                  :crit, cu1, 23:06:21, 1s
    
    section Issue #2: Vision Timeout
    Vision timeout               :crit, vt1, 23:09:29, 1s
    
    section Issue #3: Concurrent Transitions
    MOVE_TO_SCAN queued         :queued1, 23:09:21, 1s
    SCREWING_EXEC queued        :queued2, 23:09:29, 1s
    SCAN_PRODUCT queued         :queued3, 23:09:30, 1s
    
    section Issue #4: Race Condition
    DETECT_HOLES (1st entry)    :crit, dh2, 23:09:30, 1s
    DETECT_HOLES (2nd entry)     :crit, dh3, 23:09:30, 1s
    
    section Issue #5: Clean-up Conflict
    Conveyor timeout #4          :crit, ct4, 23:09:32, 1s
    Clean up #4                  :crit, cu4, 23:09:32, 1s
```

## Race Condition Detailed View

```mermaid
sequenceDiagram
    participant Loop1 as State Machine<br/>Loop Iteration 1
    participant Loop2 as State Machine<br/>Loop Iteration 2
    participant State as State Variable
    participant Flag as state_cmd_executing
    participant CQ as Command Queue
    
    rect rgb(255, 200, 200)
        Note over Loop1,Loop2: T=23:09:30.703 - Race Condition Window
        Loop1->>State: Read state = DETECT_HOLES?
        Loop2->>State: Read state = DETECT_HOLES? ⚠️ SIMULTANEOUS
        
        State-->>Loop1: Yes
        State-->>Loop2: Yes ⚠️
        
        Loop1->>Flag: Read flag = false?
        Loop2->>Flag: Read flag = false? ⚠️ SIMULTANEOUS
        
        Flag-->>Loop1: false
        Flag-->>Loop2: false ⚠️ BOTH SEE FALSE!
    end
    
    rect rgb(200, 255, 200)
        Note over Loop1: T=23:09:30.703 - Loop 1 Sets Flag
        Loop1->>Flag: store(true)
        Loop1->>Loop1: Enter DETECT_HOLES state
        Loop1->>CQ: Queue commands
        Loop1->>Loop1: Log: "DETECT_HOLES detected"
    end
    
    rect rgb(255, 200, 200)
        Note over Loop2: T=23:09:30.713 - Loop 2 Also Sets Flag (Too Late!)
        Loop2->>Flag: store(true) ⚠️ FLAG ALREADY SET!
        Loop2->>Loop2: Enter DETECT_HOLES state ⚠️ RE-ENTRY!
        Loop2->>CQ: Queue commands ⚠️ DUPLICATE!
        Loop2->>Loop2: Log: "DETECT_HOLES detected" ⚠️ DUPLICATE!
    end
    
    Note over Loop1,Loop2: Result: State entered twice, commands queued twice
```

## Concurrent State Transitions Flow

```mermaid
flowchart TD
    Start([23:09:21.824<br/>MOVE_TO_SCAN detected]) --> Queue1[Queue Transition:<br/>MOVE_TO_SCAN -> SCAN_PRODUCT]
    
    Queue1 --> Wait1[Wait for commands<br/>to execute]
    
    Wait1 --> Timeout[23:09:29.098<br/>Vision Timeout]
    
    Timeout --> ExecState[23:09:29.104<br/>SCREWING_EXECUTION_STATE]
    
    ExecState --> Queue2[Queue Transition:<br/>SCREWING_EXEC -> DETECT_HOLES]
    
    Queue2 --> Execute1[23:09:30.489<br/>Execute: MOVE_TO_SCAN -> SCAN_PRODUCT]
    
    Execute1 --> ScanState[23:09:30.491<br/>SCAN_PRODUCT_STATE]
    
    ScanState --> Queue3[Queue Transition:<br/>SCAN_PRODUCT -> DETECT_HOLES]
    
    Queue3 --> Execute2[23:09:30.700<br/>Execute: SCREWING_EXEC -> DETECT_HOLES]
    
    Execute2 --> Detect1[23:09:30.703<br/>DETECT_HOLES_STATE<br/>Entry #1]
    
    Detect1 --> Execute3[23:09:30.705<br/>Execute: SCAN_PRODUCT -> DETECT_HOLES]
    
    Execute3 --> Detect2[23:09:30.713<br/>DETECT_HOLES_STATE<br/>Entry #2 🔴 RACE!]
    
    Detect2 --> Conflict[State Confusion:<br/>Multiple entries,<br/>duplicate commands]
    
    style Timeout fill:#FFA500,stroke:#000,stroke-width:2px
    style Execute1 fill:#FF6B6B,stroke:#000,stroke-width:2px
    style Execute2 fill:#FF6B6B,stroke:#000,stroke-width:2px
    style Execute3 fill:#FF6B6B,stroke:#000,stroke-width:2px
    style Detect2 fill:#FF0000,stroke:#000,stroke-width:3px
    style Conflict fill:#FF0000,stroke:#000,stroke-width:3px
```

## Command Queue Conflict During Clean-up

```mermaid
sequenceDiagram
    participant SM as State Machine
    participant CQ as Command Queue
    participant CT as Conveyor Timer
    participant CU as Clean Up
    
    Note over SM,CU: Normal Operation
    SM->>CQ: Queue: update_system_state_screw (DETECT_HOLES -> SCREWING_EXEC)
    SM->>CQ: Queue: flush_data_queue
    SM->>CQ: Queue: detect_hole_positions
    SM->>CQ: Queue: wait_for_screw_hole_detection
    SM->>CQ: Queue: update_system_state_screw (SCAN_PRODUCT -> DETECT_HOLES)
    
    Note over SM,CU: Conveyor Timeout Occurs
    CT->>CU: Conveyor timeout detected!
    CU->>CU: clean_up() called
    
    rect rgb(255, 200, 200)
        Note over CU,CQ: Clean-up Clears Queue
        CU->>CQ: clear_command_queue()
        CQ->>CQ: Remove: update_system_state_screw (DETECT_HOLES -> SCREWING_EXEC)
        CQ->>CQ: Remove: flush_data_queue
        CQ->>CQ: Remove: detect_hole_positions
        CQ->>CQ: Remove: wait_for_screw_hole_detection
        CQ->>CQ: Remove: update_system_state_screw (SCAN_PRODUCT -> DETECT_HOLES)
    end
    
    rect rgb(255, 200, 200)
        Note over CU,SM: State Machine Unaware
        CU->>SM: (No notification)
        SM->>SM: Still thinks transitions are queued ⚠️
        SM->>SM: State becomes inconsistent 🔴
    end
    
    Note over SM,CU: Result: State machine stuck in wrong state
```

## Issue Frequency Analysis

```mermaid
pie title Issue Frequency in Log
    "Conveyor Timeouts" : 4
    "Vision Timeouts" : 1
    "Race Conditions" : 1
    "Concurrent Transitions" : 3
    "Clean-up Conflicts" : 4
```

## State Machine State Confusion

```mermaid
stateDiagram-v2
    [*] --> MOVE_TO_SCAN: 23:09:21.824
    
    MOVE_TO_SCAN --> SCAN_PRODUCT: Transition queued<br/>23:09:21.825
    
    MOVE_TO_SCAN --> SCREWING_EXEC: Vision timeout<br/>23:09:29.104
    
    SCREWING_EXEC --> DETECT_HOLES: Retry queued<br/>23:09:29.104
    
    SCAN_PRODUCT --> DETECT_HOLES: Transition queued<br/>23:09:30.491
    
    DETECT_HOLES --> DETECT_HOLES: Race condition!<br/>23:09:30.713 🔴
    
    DETECT_HOLES --> [*]: Clean-up clears queue<br/>23:09:32.452
    
    note right of SCREWING_EXEC
        Multiple transitions
        queued simultaneously
    end note
    
    note right of DETECT_HOLES
        Race condition causes
        double entry
    end note
```

## Root Cause Chain

```mermaid
flowchart TD
    A[Vision System Timeout<br/>7 seconds] --> B[State Machine Enters<br/>SCREWING_EXECUTION_STATE]
    
    B --> C[Retry Logic Queues<br/>Transition to DETECT_HOLES]
    
    D[MOVE_TO_SCAN Queues<br/>Transition to SCAN_PRODUCT] --> E[Transition Executes<br/>After Delay]
    
    E --> F[SCAN_PRODUCT Queues<br/>Transition to DETECT_HOLES]
    
    C --> G[Multiple Transitions<br/>Queued Simultaneously]
    F --> G
    
    G --> H[Transitions Execute<br/>Out of Order]
    
    H --> I[State Machine Enters<br/>DETECT_HOLES Twice]
    
    I --> J[Race Condition:<br/>10ms Double Entry]
    
    K[Conveyor Timeout] --> L[clean_up Clears<br/>Command Queue]
    
    L --> M[State Machine Unaware<br/>of Cleared Transitions]
    
    M --> N[State Inconsistency]
    
    style A fill:#FFA500,stroke:#000,stroke-width:2px
    style G fill:#FF6B6B,stroke:#000,stroke-width:2px
    style J fill:#FF0000,stroke:#000,stroke-width:3px
    style N fill:#FF0000,stroke:#000,stroke-width:3px
```

## Fix Priority Matrix

```mermaid
quadrantChart
    title Fix Priority Matrix
    x-axis Low Impact --> High Impact
    y-axis Easy Fix --> Hard Fix
    quadrant-1 Hard to Fix, High Impact
    quadrant-2 Easy Fix, High Impact
    quadrant-3 Easy Fix, Low Impact
    quadrant-4 Hard to Fix, Low Impact
    
    Race Condition: [0.9, 0.8]
    Concurrent Transitions: [0.8, 0.7]
    Clean-up Conflicts: [0.7, 0.8]
    Vision Timeout: [0.5, 0.6]
    Conveyor Timeout: [0.4, 0.5]
```

## Summary Statistics

| Issue | Occurrences | Severity | Fix Priority |
|-------|-------------|----------|--------------|
| Race Condition | 1 | 🔴 Critical | P0 |
| Concurrent Transitions | 3 | 🔴 Critical | P0 |
| Clean-up Conflicts | 4 | 🔴 Critical | P1 |
| Vision Timeout | 1 | 🟠 Medium | P2 |
| Conveyor Timeout | 4 | 🟠 Medium | P2 |

**Total Critical Issues:** 8
**Total Medium Issues:** 5

**Overall System Status:** 🔴 **Unstable** - Requires immediate fixes

