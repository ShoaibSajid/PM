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

**Note:** These targets define the minimum requirements for project acceptance. All systems must meet or exceed these criteria for successful handover.

