# Vision Pipeline: Current vs Desired Flow

## Summary

| | Current | Desired |
|---|--------|--------|
| **Input to Vision Model** | RGB only | RGB + Depth |
| **Who provides depth at (x,y)?** | Framework (lookup on depth map) | Vision model (predicts x, y, depth) |
| **Depth validation** | None | Sanity check (range, outliers) before hand-eye |
| **If depth invalid** | N/A | Fallback: depth-map lookup at (x,y) or reject |

---

## Flowchart

```mermaid
flowchart TB
  %% ============================================
  %% CURRENT FLOW
  %% ============================================
  subgraph current["Current flow"]
    direction TB
    C_cam[("Camera")]
    C_cam -->|"1. RGB"| C_fw[Framework]
    C_cam -->|"1. Depth map"| C_fw

    C_fw -->|"2. RGB only"| C_vm[Vision Model]
    C_vm -->|"3. (x, y)"| C_fw

    C_fw -->|"4. Look up depth at (x,y)"| C_dep[(Depth map)]
    C_dep -->|"depth z"| C_fw

    C_fw -->|"5. (x, y, z)"| C_he[Hand-Eye Transform]
    C_he --> C_out[Final 3D points]
  end

  %% ============================================
  %% DESIRED FLOW
  %% ============================================
  subgraph desired["Desired flow"]
    direction TB
    D_cam[("Camera")]
    D_cam -->|"1. RGB"| D_fw[Framework]
    D_cam -->|"1. Depth map"| D_fw

    D_fw -->|"2. RGB + Depth"| D_vm[Vision Model]
    D_vm -->|"3. (x, y, depth)"| D_fw

    D_fw -->|"4. Sanity check"| D_check{Depth valid?}
    D_check -->|"Yes: in range, no outlier"| D_he[Hand-Eye Transform]
    D_he --> D_out[Final 3D points]

    D_check -->|"No: out of range or invalid"| D_fb[Fallback]
    D_fb --> D_fb1["Option A: Rescan"]
    D_fb --> D_fb2["Option B: Scan Failed"]
  end
```

---

## Step-by-step

### Current flow

1. **Camera** outputs RGB image and depth map.
2. **Framework** sends only **RGB** to the vision model.
3. **Vision model** returns **(x, y)** in image space.
4. **Framework** reads **depth z** at (x, y) from the depth map.
5. **Framework** passes **(x, y, z)** to hand-eye transformation → **final 3D points**.

### Desired flow

1. **Camera** outputs RGB image and depth map.
2. **Framework** sends **RGB + Depth** to the vision model.
3. **Vision model** returns **(x, y, depth)** (depth comes from the model, not the map).
4. **Framework** runs a **depth sanity check** (range, invalid, outlier).
5. **If valid:** (x, y, z) → hand-eye transformation → **final 3D points**.
6. **If invalid:** **Fallback** — either get depth from the map at (x, y) or reject the point.

---

## What changes

- **Vision model** is depth-aware: it gets RGB + depth and outputs x, y, and depth.
- **Depth source** shifts from “always from depth map” to “from model, validated; fallback to map or reject.”
- **Validation** step ensures depth is in range and not an outlier before hand-eye transform.

---

## Vision I/O Diagram (RGB + Raw Depth → Screw Dict)

High-level inputs and output of the vision stage: RGB and raw depth go in; a per-screw dictionary comes out.

```mermaid
flowchart LR
  subgraph Inputs["Inputs"]
    RGB["RGB Image"]
    DEPTH["Depth (Raw) values"]
  end

  subgraph Vision["Vision"]
    VM["Vision Model<br/>(detector + depth read + tilt estimation)"]
  end

  subgraph Output["Output"]
    D["Dict (size = #screws)"]
    STRUCT["Per entry:<br/>Screw Number → Identifier<br/>Screw Position → (X, Y)<br/>Screw Depth → Depth value<br/>Screw Tilt → (Rx, Ry)"]
    D ~~~ STRUCT
  end

  RGB --> VM
  DEPTH --> VM
  VM --> D
```
