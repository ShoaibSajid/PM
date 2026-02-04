# Custom Pending Tasks — Screw Driver Robot

**Last updated:** February 4, 2026

---

## Planned / In progress

### Completed
- ~~**Depth Map Analysis**~~ ✅ Complete — Raw depth data provided to vision team (~50)

### Morning *(today - morning)*
1. **Integrate Top Camera** — Use Top Camera to identify if the printer is available / within range  
2. **Get Rx Ry Rz from vision model**

### Evening *(today - evening)*
3. **Fairino Collision Integration** — Integrate Fairino collision flag (not yet integrated)  
4. **Install Mirror properly** — Fixed and repeatable position (dedicated bracket if needed)  
5. **Test GUI and find potential issues**

---

## From members

*Hardware / code list from team:*

1. **GPU** — Since the new algorithm makes inference time x3 (or x4), we need a more powerful GPU.

2. **Extension part for gripper fingers** should be in **metal**, otherwise it will break after some time.

3. **SLP-DX220** (2 holes in lower layer): modify the code to calculate depth — top surface subtract a fixed value.

4. **Jalol:** Professor required a feature to adjust position of Fairino robot; movement is complex. Muazzam is using moveJ with fixed movement for every printer. If we want it per printer, need Muazzam to help.
