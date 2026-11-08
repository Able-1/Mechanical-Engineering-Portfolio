# Flight Test Results

## Test 1: Stability
**Goal:** check the drone holds a steady posture in flight and landing.
**Result:** passed. This confirmed the MPU6050 was working and correctly programmed.

## Test 2: Altitude and direction
**Result:** flew to about 70 m, then lost directional control because the front and back of the drone could not be told apart in the air. The drone crashed, damaging an arm, the propellers and an ESC.
**Root cause:** no clear visual indication of heading.
**Fix:** built a new arm and coloured the forward-facing and rear-facing arms differently.

## Test 3: Piloting
**Result:** stable flight and a positive response, then a crash-landing caused by limited navigation skill. Vital hardware and bodywork were damaged.
**Root cause:** piloting experience, and a frame that did not protect the hardware in a crash.
**Fix:** designed a new body (the "Blue Beetle") that tolerates multiple crashes, protects vital hardware and makes flight direction easy to identify at any time.

## Takeaway
Proper flight was achieved after a series of failures. Each failure had one identifiable cause, and each fix went into the next design iteration.
