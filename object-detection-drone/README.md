# Object Detection Drone: 3D-Printed Quadcopter

**Final-year B.Eng group project · Mechanical Engineering · University of Benin · 2023**

This project involved developing a 3D-printed quadcopter prototype with an Arduino-based control system, an MPU6050 motion sensor and an OpenMV H7 Plus camera. The camera implementation performed frontal-face detection and activated an LED/alarm output when a face was detected.

The project brought together mechanical design, structural analysis, 3D printing, electronics integration, computer vision and iterative testing.

![Blue Beetle CAD render](images/blue-beetle-cad-render.png)

> **Team project:** completed by a group of four students. This page describes the overall project. It does not assign unverified individual contributions.

## Project overview

| Area | Details |
|---|---|
| Platform | Quadcopter prototype |
| Frame | 3D-printed PLA |
| Control hardware | Arduino Uno |
| Motion sensor | MPU6050 |
| Camera | OpenMV Cam H7 Plus |
| Vision task | Frontal-face detection using a Haar cascade |
| Propulsion | Four brushless motors with ESCs |
| Radio control | FlySky i6X transmitter and receiver |
| Project cost | ₦430,900 as stated in the report; see [bill of materials](hardware/bill-of-materials.md) |

## Project objectives

1. Design a lightweight quadcopter frame.
2. Model and assess the frame before manufacture.
3. Manufacture the frame using 3D printing.
4. Integrate the propulsion, control and power components.
5. Add a camera-based face-detection function.
6. Conduct flight tests and improve the design based on observations.

## Design and analysis

The team modelled the frame components in CAD and carried out structural stress, strain and displacement studies. The analysis was used to assess the proposed frame before 3D printing.

| Displacement study | Stress study |
|---|---|
| ![Displacement analysis](images/displacement-analysis-2.png) | ![Stress analysis](images/stress-analysis.png) |

The prototype frame was printed in PLA. PLA made it practical to produce and revise parts, although its impact resistance and heat tolerance are limitations to consider in a flying prototype.

## Hardware

| Component | Purpose |
|---|---|
| Arduino Uno | Control-system integration |
| MPU6050 | Accelerometer and gyroscope measurements |
| Brushless motors | Propulsion |
| Electronic speed controllers | Motor-speed control |
| LiPo battery and power distribution board | Electrical power |
| FlySky transmitter and receiver | Pilot input |
| OpenMV Cam H7 Plus | On-board image processing |

![OpenMV H7 Plus](images/openmv-h7-plus.png)
![Arduino Uno](images/arduino-uno.png)

## Face-detection function

The camera implementation used a Haar-cascade frontal-face detector. When a face was detected, the program set an output pin to activate an LED and alarm.

The included [face_detect.py](software/openmv/face_detect.py) is a reconstructed example based on the project documentation; it should not be treated as the original source code from the project.

**Scope note:** this prototype demonstrated frontal-face detection. It was not a general-purpose object-detection system.

## Flight testing and iteration

The project documentation records three rounds of testing:

| Test | Reported observation | Design response |
|---|---|---|
| Initial stability test | The prototype achieved a stable flight and landing during the test. | Continued testing. |
| Altitude test | The drone reportedly reached approximately 70 metres, lost orientation and crashed. | Repaired damaged parts and added colour cues to help distinguish the front and rear. |
| Further flight test | The drone was reported to be stable and responsive, but crashed during landing. | The team developed a revised frame design referred to as “Blue Beetle”. |

| Initial test | Damage after a test | Revised printed frame |
|---|---|---|
| ![Flight test](images/flight-test-1-stability.png) | ![Crash damage](images/flight-test-2-crash-damage.png) | ![Blue Beetle printed frame](images/blue-beetle-printed-frame.png) |

These are observations recorded in the project report, not independently measured performance results. Further detail is available in [flight-test results](results/flight-test-results.md).

## Challenges and lessons

- Maintaining clear orientation cues for the pilot.
- Managing damage to the frame and components during testing.
- Sourcing components and working within the project budget.
- Integrating the camera function with the wider prototype.
- Using test observations to guide design changes.

The project reinforced the importance of designing for maintainability and impact resistance, documenting test conditions, and separating mechanical, electrical and software faults during troubleshooting.

## Full academic report

A privacy-reviewed copy of the 2023 project report has been prepared. The student numbers and the other students’ names have been removed from the public-sharing copy; the author’s name and university/project details remain. The PDF is not yet stored in this repository. See [report documentation](report/README.md) for the report scope and access note.

## Design files and project evidence

The repository currently contains selected analysis images and project photographs. Original CAD models, manufacturing drawings and the complete original source code are not included at present. See the [design folder](design/README.md) for the files that can be added when available.

## Accuracy and limitations

- The project was completed by a team of four; individual contributions should be described separately and only where confirmed.
- The original project objectives mention carbon-fibre filament, but the documented prototype frame was printed in PLA.
- The motion sensor is identified as an MPU6050 in the component descriptions; the report contains an inconsistent “MPU6040” reference.
- The vision feature described here is frontal-face detection, not general object detection.
- The cost breakdown is transcribed from the report and contains inconsistencies; it has not been verified against receipts.
- The reported flight observations are presented as documented project outcomes, not independently validated measurements.

## Tools and technologies

SolidWorks · AutoCAD · PLA 3D printing · Arduino Uno · OpenMV IDE · Python
