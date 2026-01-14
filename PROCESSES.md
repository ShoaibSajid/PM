# Processes & Acceptance

## Acceptance

```mermaid
stateDiagram-v2
  [*] --> CycleStart
  CycleStart --> Execute
  Execute --> Completed: Completed within cycle time
  Execute --> Warning: Incomplete / Error
  Completed --> [*]
  Warning --> [*]
```

**Acceptance Rules**
- Each robot is evaluated independently
- Completion within cycle time = PASS
- Any incomplete cycle = WARNING

---

## Vision Validation Workflow

Vision validation is treated as a production-readiness gate and is performed on 10–20 real products per system.

```mermaid
flowchart TB
  V0[Assign Validation Task]
  V0 --> V1[Confirm Model Details]
  V1 --> V2[Confirm Integration Status]
  V2 --> V3[Test on 10–20 Products]
  V3 --> V4[Calculate Accuracy]
  V4 --> V5{Any failures?}
  V5 -- No --> V6[PASS Recommendation]
  V5 -- Yes --> V7[Failure Analysis]
  V7 --> V8{Retraining needed?}
  V8 -- Yes --> V9[Retrain / Tune Model]
  V8 -- No --> V6
```

**Validation Output**
- Robot system name
- Vision model name and version
- Integration status
- Accuracy results
- Failure cases and root cause
- Pass / Fail conclusion

---

[← Back to Overview](./README.md)

