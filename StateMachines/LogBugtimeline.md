# Log Bug Timeline Diagram

This document visualizes all bug occurrences throughout the full log file timeline.

## Bug Occurrence Timeline

```mermaid
timeline
    title State Machine Bug Occurrences Over Time
    
    section 17:45-17:46
        SCREWING_EXECUTION : 380 total entries
                          : Rapid re-entry (3x in 313ms)
                          : Race condition (10ms)
        PRESSING_ARM_DOWN : 3x re-entry (282ms intervals)
        COMPLETED_STATE   : 1x entry
        
    section 17:57-17:59
        SCREWING_EXECUTION : Multiple rapid entries
                          : Race conditions detected
        COMPLETED_STATE   : 1x entry
        
    section 18:01-18:08
        SCREWING_EXECUTION : Many rapid entries
                          : 4x in 21ms (race condition)
                          : Multiple 10ms intervals
        COMPLETED_STATE   : Multiple entries
        IDLE              : Multiple rapid entries
        
    section 19:23-19:40
        SCREWING_EXECUTION : Multiple entries
        PRESSING_ARM_DOWN : 3x re-entry (282ms)
        COMPLETED_STATE   : Multiple entries
        
    section 21:49-21:51
        COMPLETED_STATE   : 4x re-entry (759ms) 🔴 CRITICAL
        IDLE              : 4x rapid entries
        PRESSING_ARM_DOWN : 3x re-entry (565ms)
        SCAN_PRODUCT      : 2x re-entry (868ms)
        DETECT_HOLES      : 2x race condition (10ms) 🔴 CRITICAL
```

## Bug Frequency Heatmap

```mermaid
graph LR
    subgraph "Bug Severity by State"
        A[SCREWING_EXECUTION_STATE<br/>380 occurrences<br/>🔴 CRITICAL] -->|Most Frequent| B[Missing Execution Flag]
        C[COMPLETED_STATE<br/>27 occurrences<br/>🔴 CRITICAL] -->|4x Re-entry| D[Double Transition Bug]
        E[IDLE State<br/>118 occurrences<br/>🟠 HIGH] -->|Multiple Entries| F[Re-entry After Completion]
        G[PRESSING_ARM_DOWN<br/>31 occurrences<br/>🟠 HIGH] -->|3x Pattern| H[Missing Guards]
        I[Race Conditions<br/>10+ instances<br/>🔴 CRITICAL] -->|10ms Intervals| J[Concurrent Execution]
    end
    
    style A fill:#FF0000,stroke:#000,stroke-width:3px,color:#FFF
    style C fill:#FF0000,stroke:#000,stroke-width:3px,color:#FFF
    style I fill:#FF0000,stroke:#000,stroke-width:3px,color:#FFF
    style E fill:#FF6B00,stroke:#000,stroke-width:2px
    style G fill:#FF6B00,stroke:#000,stroke-width:2px
```

## Detailed Bug Pattern Visualization

```mermaid
flowchart TD
    Start([Log Analysis Start]) --> Parse[Parse Log Entries]
    Parse --> CheckSCREWING{SCREWING_EXECUTION_STATE?}
    Parse --> CheckCOMPLETED{COMPLETED_STATE?}
    Parse --> CheckIDLE{IDLE State?}
    Parse --> CheckPRESSING{PRESSING_ARM_DOWN?}
    Parse --> CheckRACE{Race Condition?}
    
    CheckSCREWING -->|380 times| Bug1[🐛 BUG #1: Missing Execution Flag<br/>Line 103 commented out<br/>Allows unlimited re-entry]
    Bug1 --> Impact1[Impact: State entered 380x<br/>vs expected ~50-100x]
    
    CheckCOMPLETED -->|27 times| Bug2[🐛 BUG #2: Double State Transition<br/>Lines 628-634<br/>Execution + Main state transition]
    Bug2 --> Impact2[Impact: 4x re-entry in 759ms<br/>State machine instability]
    
    CheckIDLE -->|118 times| Bug3[🐛 BUG #3: Re-entry After Completion<br/>State machine continues after completion]
    Bug3 --> Impact3[Impact: Multiple IDLE entries<br/>System doesn't properly stop]
    
    CheckPRESSING -->|31 times| Bug4[🐛 BUG #1: Missing Execution Flag<br/>Allows 3x re-entry pattern]
    Bug4 --> Impact4[Impact: Consistent 3x pattern<br/>282ms intervals]
    
    CheckRACE -->|10+ instances| Bug5[🐛 BUG #1: Race Condition<br/>10ms double entries<br/>Missing execution guards]
    Bug5 --> Impact5[Impact: Concurrent execution<br/>Unpredictable behavior]
    
    Impact1 --> Summary[Summary: All Bugs Confirmed<br/>Critical System Failure]
    Impact2 --> Summary
    Impact3 --> Summary
    Impact4 --> Summary
    Impact5 --> Summary
    
    style Bug1 fill:#FF0000,stroke:#000,stroke-width:3px,color:#FFF
    style Bug2 fill:#FF0000,stroke:#000,stroke-width:3px,color:#FFF
    style Bug3 fill:#FF6B00,stroke:#000,stroke-width:2px
    style Bug4 fill:#FF6B00,stroke:#000,stroke-width:2px
    style Bug5 fill:#FF0000,stroke:#000,stroke-width:3px,color:#FFF
    style Summary fill:#FF6B6B,stroke:#000,stroke-width:3px
```

## State Entry Frequency Analysis

```mermaid
pie title State Entry Frequency (Bug vs Normal)
    "SCREWING_EXECUTION (Bug)" : 380
    "IDLE (Bug)" : 118
    "PRESSING_ARM_DOWN (Bug)" : 31
    "COMPLETED_STATE (Bug)" : 27
    "Expected Normal Entries" : 50
```

## Race Condition Detection

```mermaid
sequenceDiagram
    participant Loop1 as State Machine Loop (Thread 1)
    participant Loop2 as State Machine Loop (Thread 2)
    participant State as Current State
    participant Flag as state_cmd_executing Flag
    
    Note over Loop1,Loop2: Both loops running concurrently
    
    Loop1->>State: Check state = SCREWING_EXECUTION?
    Loop2->>State: Check state = SCREWING_EXECUTION?
    
    State-->>Loop1: Yes, !state_cmd_executing
    State-->>Loop2: Yes, !state_cmd_executing ⚠️
    
    Note over Flag: Flag NOT set! (Line 103 commented)
    
    Loop1->>Loop1: Enter SCREWING_EXECUTION_STATE
    Loop2->>Loop2: Enter SCREWING_EXECUTION_STATE ⚠️ RACE!
    
    Note over Loop1,Loop2: Both enter within 10ms!
    
    Loop1->>Loop1: Call screw_execution_state()
    Loop2->>Loop2: Call screw_execution_state() ⚠️ CONCURRENT!
```

## Bug Manifestation Flow

```mermaid
flowchart LR
    A[State Machine Loop] -->|Every iteration| B{Check State}
    B -->|SCREWING_EXECUTION| C{state_cmd_executing?}
    C -->|NOT SET ⚠️| D[Enter State]
    C -->|Should be set| E[Skip - Already Executing]
    
    D --> F[Call screw_execution_state]
    F --> G[State Machine Continues]
    G -->|Next iteration| B
    
    D --> H[Race Condition Risk]
    H -->|10ms later| I[Another Loop Iteration]
    I -->|Sees same state| D
    
    style C fill:#FF6B6B,stroke:#000,stroke-width:2px
    style D fill:#FF0000,stroke:#000,stroke-width:3px,color:#FFF
    style H fill:#FF0000,stroke:#000,stroke-width:3px,color:#FFF
```

## Critical Bug Instances Summary

| Instance | Time | State | Count | Interval | Severity |
|----------|------|-------|-------|----------|----------|
| #1 | 21:50:38-39 | COMPLETED_STATE | 4x | 61-636ms | 🔴 CRITICAL |
| #2 | 17:46:09-10 | PRESSING_ARM_DOWN | 3x | 282-283ms | 🟠 HIGH |
| #3 | 19:39:55 | PRESSING_ARM_DOWN | 3x | 282ms | 🟠 HIGH |
| #4 | 21:51:12-13 | PRESSING_ARM_DOWN | 3x | 282-283ms | 🟠 HIGH |
| #5 | 17:45:51 | SCREWING_EXECUTION | 3x | 10-21ms | 🔴 CRITICAL |
| #6 | 18:01:56 | SCREWING_EXECUTION | 3x | 10-41ms | 🔴 CRITICAL |
| #7 | 18:02:00 | SCREWING_EXECUTION | 4x | 10-21ms | 🔴 CRITICAL |
| #8 | 18:06:05 | SCREWING_EXECUTION | 4x | 10-21ms | 🔴 CRITICAL |
| #9 | 21:51:21 | DETECT_HOLES | 2x | 10ms | 🔴 CRITICAL |
| #10 | Multiple | IDLE | 4x | 11ms-2.3s | 🟠 HIGH |

## Conclusion

The log analysis reveals **systematic and widespread** state machine bugs:

1. **380 SCREWING_EXECUTION_STATE entries** - Should be ~50-100 for normal operation
2. **Multiple race conditions** - 10ms intervals indicate concurrent execution
3. **Consistent re-entry patterns** - 3x PRESSING_ARM_DOWN with 282ms intervals
4. **4x COMPLETED_STATE re-entry** - Critical state machine failure
5. **118 IDLE entries** - System doesn't properly stop after completion

**All bugs identified in code analysis are confirmed by runtime logs.**

