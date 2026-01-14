# Everint Project – Status Report

**Client:** Everint (company name)  
**Project Owner:** Shoaib (recently joined to manage all teams)  
**Last Updated:** January 2026  
**Project Phase:** Validation, Acceptance, and Handover

---

## Project Overview

The Everint project involves the deployment, validation, and handover of multiple **industrial robotic systems** used for automated assembly operations at Everint factory. Each robot system operates **independently** and is evaluated based on **cycle-time-driven acceptance criteria**.

**Robot Systems:**
- **PCB Screw Robot:** Scans product, identifies screw holes, performs automated screwing
- **Label Printer Screw Robot:** Identifies screw holes on product body and screws them
- **Rubber Foot Robot:** Attaches rubber pads to product body (placed after Label Printer Screw Robot)

A robot cycle is considered **PASS** if:
- All required actions are completed (all screws fastened / all rubber pads attached)
- The cycle completes within the predefined cycle time for the given product type

If a cycle cannot be completed for any reason, the system **raises a warning**.  
Sequential handover between robots is **not required**.

---

## Overall Status Summary

- **Implementation:** Complete
- **Validation:** In progress
- **Documentation:** In progress
- **Risk Level:** Low to Medium (primarily validation and handover completeness)

The project is transitioning from execution to formal acceptance and ownership transfer, with remaining work focused on evidence, documentation, and clarity rather than new development.

---

## Documentation Structure

This project documentation is organized into the following files:

- **[SYSTEMS.md](./SYSTEMS.md)** - Detailed information about each robotic system, architecture, and operational flows
- **[PROCESSES.md](./PROCESSES.md)** - Acceptance criteria and vision validation workflows
- **[TEAM_AND_HANDOVER.md](./TEAM_AND_HANDOVER.md)** - Team structure, handover package, definition of done, and current focus areas
- **[URGENT_TASKS.md](./URGENT_TASKS.md)** - Most urgent tasks extracted from project communications
- **[URGENT_ISSUES_CHECKLIST.md](./URGENT_ISSUES_CHECKLIST.md)** - Visual checklist of urgent issues (headlines only)
- **[JAN_15_CHECKLIST.md](./JAN_15_CHECKLIST.md)** - Daily checklist for January 15, 2026
- **[MISSING_ITEMS.md](./MISSING_ITEMS.md)** - Gaps and missing items that need attention
- **[RULES.md](./RULES.md)** - Project coordination rules and guidelines

---

## Quick Links

- [Robotic Systems](./SYSTEMS.md#robotic-systems-in-scope)
- [System Architecture](./SYSTEMS.md#high-level-system-architecture)
- [Acceptance Criteria](./PROCESSES.md#acceptance)
- [Vision Validation](./PROCESSES.md#vision-validation-workflow)
- [Team Structure](./TEAM_AND_HANDOVER.md#team-structure-and-ownership)
- [Handover Package](./TEAM_AND_HANDOVER.md#documentation--handover-package)
- [Definition of Done](./TEAM_AND_HANDOVER.md#definition-of-done)
- [Urgent Tasks](./URGENT_TASKS.md)
- [Urgent Issues Checklist](./URGENT_ISSUES_CHECKLIST.md)
- [Jan 15 Checklist](./JAN_15_CHECKLIST.md)
- [Missing Items](./MISSING_ITEMS.md)
- [Coordination Rules](./RULES.md)
