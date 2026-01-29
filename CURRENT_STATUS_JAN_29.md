# Current Status & Today's Tasks - January 29, 2026

---

## 📊 Current Status (Bullet Points)

### ✅ Completed Yesterday (Jan 28)
- **Reflection analysis completed** - Tan identified and mitigated 3 main reflection causes affecting screw holes
- **RealSense JSON configuration tuned** - Separate config created, ready for testing today
- **Metal FR3 finger base parts received** - Ready for installation
- **Metal 3D printing mesh part received** - Dr Saad's requested part
- **Plate for thin plate attachment received** - Can change from nut to plate
- **Scooping claw analysis completed** - Muazzam identified 4 redesign requirements

### 🔴 Critical Issues
- **Depth map reflection** - Partially mitigated, needs testing with JSON config today
- **Fairino collision signal** - Developed but not integrated into main framework
- **Depth outlier filtering** - Need to implement expected-value logic for depth accuracy
- **Scooping claw redesign** - 4 specific requirements identified, needs redesign
- **GUI testing incomplete** - Delayed due to depth tuning experiments

### 🟡 High Priority Issues
- **Upper lights too bright** - Need to suggest removal to manager
- **GUI layout refinement** - Cluttered layout, inconsistent button sizes
- **Hardware installation** - Metal parts ready but not installed
- **Code integration** - Screw/rubber code merge pending

---

## 📋 Today's Tasks (January 29, 2026)

### 🔴 Critical Tasks

#### Screw Robot (Tan, Hieu, Ammad)
- **Test RealSense JSON configuration** - Verify tuned config works properly
- **Integrate Fairino collision signal** - Integrate into main framework
- **Add depth outlier filtering logic** - Implement expected-value logic as Professor suggested
- **Test GUI and find issues** - Complete GUI testing (delayed from yesterday)
- **Capture depth maps with different light settings** - Continue testing with own light

#### Rubber Foot Robot (Tugi, Muazzam, Myeongun)
- **Redesign scooping claw and bracket** - Address 4 identified requirements:
  - Bracket base seating on metal bracket
  - Extend bracket for proper scooping
  - Redesign claw (flat instead of tilted)
  - Align hole positions properly
- **Install finger gripper** - Install hardware
- **Merge code between screw/rubber** - Run and test merged code
- **Grind/scrub sheet roller** - Hardware maintenance

#### Hardware (Muazzam, Myeongun)
- **Install metal FR3 finger base parts** - Install received parts
- **Change plate attachment** - Change from nut to plate
- **3D print dual fingers for scoop** - Determine tilt angle, share with Dr Saad
- **3D print catching basket** - Design and print
- **Sheet clamp design** - Design and print for curving/bending sheet

### 🟡 High Priority Tasks

#### Vision & System (Tan, Kwanghyeop)
- **Suggest removing upper lights** - Request manager to remove two bright upper lights
- **Bring own light for testing** - Test with different light setup
- **Refine GUI layout** - Fix cluttered layout, standardize button sizes

#### Integration & Development (Hieu, Tugi)
- **Add time estimation function** - Dump time info in json/yaml for both systems
- **Check vision parameters change from GUI** - Verify GUI parameter changes work
- **Integrate top camera** - Complete integration

#### Hardware Optimization (Tugi, Muazzam)
- **Reposition platform/rubber pad holders** - Allow 3 holders on platform
- **Test continuous supply of rubber sheet** - Verify sheet supply mechanism

---

## 🎯 Focus Areas Today

1. **Depth Map Testing** - Test JSON config and verify reflection mitigation
2. **Fairino Integration** - Complete collision signal integration
3. **Hardware Installation** - Install received metal parts
4. **Scooping Mechanism** - Redesign based on analysis
5. **GUI Completion** - Complete delayed GUI testing

---

**Last Updated:** January 29, 2026

