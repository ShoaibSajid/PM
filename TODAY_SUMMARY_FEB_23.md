# Everint Today Summary (2026-02-23)

**Source baseline:** Meeting notes received on 2026-02-23 (Rubber Foot Robot + Screw)

---

## Today Meeting Notes

### Rubber Foot Robot

1. Add half offset when adjusting.
2. At cycle start, if second shot is enabled, capture an additional image at lower scan position, then capture from home position; provide both to vision, then use lower scan for lower rubbers and normal scan for upper rubbers after vision code is ready.
3. If possible in debug mode, capture images after placing rubber (4 rubbers).
4. Track elapsed and last cycle time, and if remaining time is more than 5 seconds, capture all rubbers from high position.
5. Screw down/fix the sponge to hold pallets.
6. In dispenser logic, finish one dispenser before moving to the next dispenser.
7. Add a test bench that keeps holding the printer, identifies rubber positions, picks and attaches rubbers, and repeats the cycle without releasing the printer (to verify dispenser offset vs placement offset).

### Screw

1. Later: after the second light controller is purchased and available, increase exposure time or control light.

---

## Action Packaging For Tracking

- Rubber Foot: offset tuning update (half-offset adjustment policy) and second-shot dual-position image capture flow.
- Rubber Foot: optional debug capture after placement of all four rubbers.
- Rubber Foot: cycle-time-aware extra capture rule (if remaining time > 5s, high-position full capture).
- Rubber Foot: hardware stabilization by fixing sponge for pallet holding.
- Rubber Foot: dispenser sequencing rule to complete one dispenser before switching.
- Rubber Foot: no-release repeat-cycle test bench for placement offset isolation.
- Screw: lighting/exposure upgrade dependency after second controller procurement.
