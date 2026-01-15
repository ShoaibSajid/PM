# Everint Project - Vision System Demo Requirements

**Last Updated:** January 15, 2026  
**Purpose:** Define project targets and success criteria for vision system demo readiness

---

## Objective

Ensure demo readiness of the Everint Project by validating high-accuracy vision models, automation pipelines, and rapid retraining capabilities across multiple product types.

---

## Vision Models and Accuracy Targets

### 1. Screw Tilt Detection
- **False Negative (FN):** Not acceptable
- **False Positive (FP):** Low frequency acceptable
- **Accuracy Target:** ≥ 98%

### 2. Screw Hole Detection (with rescanning)
- **False Negative (FN):** Acceptable (rescanning supported)
- **False Positive (FP):** Not acceptable (risk of product damage)
- **Accuracy Target:** ≥ 99%

### 3. Rubber Foot Hole & Attachment Detection (with rescanning)
- **False Negative (FN):** Acceptable
- **False Positive (FP):** ≤ 10 per 1,000 products
- **Accuracy Target:** ≥ 99%

### 4. Printer Contour Detection
- **Approach:** Multi-pipeline approach using Template Matching (TM) and YOLO
- **Rescanning:** Enabled; contour must be detected within a few attempts

---

## Automation Scope

- **Full automation** of product registration is required
- **Exception:** Printer contour detection may remain semi-automatic

---

## Model Retraining and Evaluation

- All models must support retraining for new products
- **Self-training time:** ≤ 20 minutes per product
- **Automatic evaluation** against existing benchmark must be performed after retraining to verify performance

---

## Validation and KPIs

- **Minimum validation:** 100 products per product type (more preferred)
- **KPIs include:**
  - Accuracy
  - FP/FN rates
  - Product-level pass/fail metrics
- **Results must demonstrate** compliance with all defined performance thresholds

---

## Demo Success Criteria

The demo is successful if:
1. All vision models meet accuracy and error constraints
2. Retraining and evaluation complete within time limits (≤ 20 minutes per product)
3. System performance is validated on real products (minimum 100 products per type)

---

## Acceptance Criteria Summary

| Vision Model | Accuracy Target | FN Acceptable? | FP Acceptable? | Notes |
|-------------|----------------|----------------|----------------|-------|
| Screw Tilt Detection | ≥ 98% | ❌ No | ✅ Low frequency | Critical for safety |
| Screw Hole Detection | ≥ 99% | ✅ Yes (rescan) | ❌ No | FP risks product damage |
| Rubber Foot Detection | ≥ 99% | ✅ Yes (rescan) | ✅ ≤ 10/1000 | Rescanning supported |
| Printer Contour | - | ✅ Yes (rescan) | - | Multi-pipeline (TM + YOLO) |

---

## Target Achievement Tracking

**Owner Summary:**
- **Vision Model Accuracy Targets:** Rizwan
- **Automation & Registration:** Jalol
- **Model Retraining:** Rizwan
- **Validation & Testing:** Tugi and Hieu, Saad/Odil/Shoaib (KPI)
- **System Integration:** Tugi and Hieu
- **Documentation & Handover:** Kwanghyeop
- **Hardware & Installation:** Muazzam, Myeongun (Spares), Myeongun (Spares)
- **Overall Project Status:** Shoaib

---

### Vision Model Accuracy Targets (Owner: Rizwan)

| # | Target/Goal | Achieved | Progress | Notes |
|---|-------------|----------|----------|-------|
| 1 | Screw Tilt Detection: ≥ 98% accuracy, FN not acceptable | ❌ False | 0% | Validation pending |
| 2 | Screw Hole Detection: ≥ 99% accuracy, FP not acceptable | ❌ False | 0% | Validation pending |
| 3 | Rubber Foot Detection: ≥ 99% accuracy, FP ≤ 10/1000 | ❌ False | 0% | Validation pending |
| 4 | Printer Contour Detection: Multi-pipeline (TM + YOLO) with rescanning | ❌ False | 60% | Integration in progress |
| 5 | Eliminate vision errors (using secondary checks if needed) | ❌ False | 0% | Not implemented yet |

### Automation & Registration (Owner: Jalol)

| # | Target/Goal | Achieved | Progress | Notes |
|---|-------------|----------|----------|-------|
| 6 | Full automation of product registration | ❌ False | 80% | GUI issues being resolved |
| 7 | Printer contour detection (semi-automatic acceptable) | ❌ False | 70% | In progress |

### Model Retraining (Owner: Rizwan)

| # | Target/Goal | Achieved | Progress | Notes |
|---|-------------|----------|----------|-------|
| 8 | All models support retraining for new products | ❌ False | 0% | Not validated |
| 9 | Self-training time ≤ 20 minutes per product | ❌ False | 0% | Not validated |
| 10 | Automatic evaluation after retraining | ❌ False | 0% | Not validated |

### Validation & Testing (Owners: Tugi and Hieu, Saad/Odil/Shoaib)

| # | Target/Goal | Achieved | Progress | Notes |
|---|-------------|----------|----------|-------|
| 11 | Minimum 100 products per product type validated | ❌ False | 0% | Dataset collection pending |
| 12 | Vision model validation reports completed | ❌ False | 30% | In progress (Rizwan) |
| 13 | Cycle time validation for all robots | ❌ False | 25% | Rubber Foot: ~28 sec (done), Screw Robot: pending |
| 14 | Mechanism to measure KPI (products ran, success count, failure count, cycle time) | ❌ False | 0% | Not implemented yet (Saad/Odil/Shoaib) |

### System Integration (Owners: Tugi and Hieu)

| # | Target/Goal | Achieved | Progress | Notes |
|---|-------------|----------|----------|-------|
| 15 | Robot teaching completed for all systems | ❌ False | 50% | Rubber Foot: done, Screw Robot: in progress |
| 16 | Vision model integration completed | ❌ False | 60% | Integration in progress |
| 17 | Rescan logic tested and validated | ❌ False | 40% | Needs testing |
| 18 | Production ready system for all the printers | ❌ False | 60% | In progress (Tugi and Hieu) |
| 19 | Minimize failures for screw and rubber feet pickup/fasten/attach (retry at least once for all products) | ❌ False | 40% | Retry logic needs validation (Tugi and Hieu) |
| 20 | System stability: No crashes, graceful abort and warning on time-up | ❌ False | 50% | Testing to be done by Ammad (Tugi and Hieu) |

### Documentation & Handover (Owner: Kwanghyeop)

| # | Target/Goal | Achieved | Progress | Notes |
|---|-------------|----------|----------|-------|
| 21 | Handover documentation package complete | ❌ False | 0% | Not started yet (Kwanghyeop) |
| 22 | Equipment inventory with serial numbers | ❌ False | 0% | Not started yet |
| 23 | 3D parts list complete | ❌ False | 60% | In progress (Muazzam, Ammad) |
| 24 | Operation manual complete | ❌ False | 0% | Not started yet (part of handover package) |
| 25 | Maintenance guide complete | ❌ False | 0% | Not started yet (part of handover package) |
| 26 | Vision system documentation complete | ❌ False | 0% | Not started yet (part of handover package) |
| 27 | Network diagram complete | ❌ False | 0% | Not started yet |

### Hardware & Installation (Owners: Muazzam, Myeongun)

| # | Target/Goal | Achieved | Progress | Notes |
|---|-------------|----------|----------|-------|
| 28 | All hardware installed and operational | ❌ False | 85% | Screw Driver Robot fingers pending |
| 29 | Pad holding bracket fixed (Rubber Foot Robot) | ❌ False | 0% | Broken, needs replacement |
| 30 | All safety equipment installed | ❌ False | 90% | Safety fences received, installation pending |
| 31 | Prepare enough spares for key components (particularly all plastic/3D printed items) | ❌ False | 30% | In progress (Myeongun) |

### Overall Project Status (Owner: Shoaib)

| # | Target/Goal | Achieved | Progress | Notes |
|---|-------------|----------|----------|-------|
| 32 | All acceptance criteria met | ❌ False | 35% | Multiple targets pending |
| 33 | Demo readiness achieved | ❌ False | 30% | Validation, testing, and documentation in progress |

**Legend:**
- ✅ True = Target achieved
- ❌ False = Target not yet achieved
- Progress = Estimated completion percentage based on current status

**Last Updated:** January 15, 2026

---

**Note:** These targets define the minimum requirements for project acceptance. All systems must meet or exceed these criteria for successful handover. Progress percentages are estimates based on current project status and may change as work progresses.

