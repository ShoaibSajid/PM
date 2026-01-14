# Team Structure & Handover

## Team Structure and Ownership

```mermaid
flowchart TB
  subgraph PCB_SYS[PCB Screw Robot]
    A1[Ammad - Robot]
    A2[Tan - Vision]
    A3[Jalol - Backend]
    A4[Samrah - Frontend]
  end

  subgraph LP_SCREW[Label Printer - Screw Robot]
    B1[Hieu - Robot]
    B2[Rizwan / Shams - Vision]
    B3[Jalol - Backend]
    B4[Samrah - Frontend]
  end

  subgraph LP_RF[Label Printer - Rubber Foot Robot]
    C1[Tugi - Robot]
    C2[Rizwan / Sajjad - Vision]
    C3[Jalol - Backend]
    C4[Samrah - Frontend]
  end
```

**Cross-Cutting Roles**
- Shoaib: Project manager (recently joined to manage all teams), coordination, acceptance, handover
- Saad: Robot team lead
- Odil: Vision team lead
- Kwanghyeop: Local Korean engineer, supports local tasks requiring Korean language, documentation assistance
- Muazzam: Hardware support

**Note:** PCB system team members (Ammad, Tan) are currently helping other robot systems (Hieu, Tugi) as PCB system is almost complete.

---

## Documentation & Handover Package

```mermaid
flowchart LR
  D0[Handover Package]
  D0 --> D1[Operation Manual]
  D0 --> D2[Maintenance Guide]
  D0 --> D3[Equipment List]
  D0 --> D4[Vision System Details]
  D0 --> D5[System Overview]
  D0 --> D6[Support & Escalation Info]
```

**Handover Includes**
- System startup and shutdown
- Normal operation procedures
- Warning and recovery behavior
- Preventive maintenance
- Installed equipment inventory (robots, controllers, cameras)
- Camera and lighting setup
- Support ownership and escalation path

---

## Current Focus Areas

- Completion of robot teaching where still in progress
- Vision model validation and reporting
- Cycle time optimization and confirmation
- Documentation and inventory completion
- Internal acceptance review and evidence collection

---

## Definition of "Done"

A system is considered ready for handover when:

```mermaid
flowchart TB
  R0[Ready for Handover?]
  R0 --> R1{Teaching Complete?}
  R1 -- No --> R1a[Finish Teaching]
  R1 -- Yes --> R2{Vision Validation PASS?}
  R2 -- No --> R2a[Fix Vision Issues]
  R2 -- Yes --> R3{Cycle Time Met?}
  R3 -- No --> R3a[Optimize Cycle]
  R3 -- Yes --> R4{Docs & Inventory Complete?}
  R4 -- No --> R4a[Complete Handover Docs]
  R4 -- Yes --> R5[Handover Ready ✅]
```

---

[← Back to Overview](./README.md)

