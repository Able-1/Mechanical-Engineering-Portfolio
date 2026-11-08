# Design and Development of an Object Detection Drone

**Final-year B.Eng project · Mechanical Engineering · University of Benin · 2023**

For my final-year project, I worked with three other students on the design and development of a quadcopter drone. We designed the frame, carried out structural analysis, 3D-printed the prototype, assembled the main electronic components and carried out flight tests.

We also integrated an OpenMV H7 Plus camera for frontal-face detection. When the camera detected a face, the program triggered an LED and an alarm.

![Blue Beetle CAD render](images/blue-beetle-cad-render.png)

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
| Project cost | ₦430,900 as stated in the report; see the [bill of materials](hardware/bill-of-materials.md) |

## What we set out to do

1. Design a lightweight frame for the quadcopter.
2. Model the frame and study its structural behaviour.
3. Manufacture the frame using 3D printing.
4. Assemble the propulsion, control and power components.
5. Integrate a camera-based face-detection feature.
6. Test the drone and make changes based on the results.

## CAD design and structural analysis

We modelled the drone frame in CAD and carried out stress, strain and displacement analysis before manufacturing the prototype. The analysis images below are taken from the project work.

| Displacement study | Stress study |
|---|---|
| ![Displacement analysis](images/displacement-analysis-2.png) | ![Stress analysis](images/stress-analysis.png) |

The frame was printed in PLA. This allowed us to produce the parts and make changes during development.

## Hardware and assembly

The main components used in the prototype included:

| Component | Purpose |
|---|---|
| Arduino Uno | Control-system integration |
| MPU6050 | Accelerometer and gyroscope measurements |
| Brushless motors | Propulsion |
| Electronic speed controllers | Motor-speed control |
| LiPo battery and power distribution board | Electrical power |
| FlySky transmitter and receiver | Pilot input |
| OpenMV Cam H7 Plus | Image processing |

![OpenMV H7 Plus](images/openmv-h7-plus.png)
![Arduino Uno](images/arduino-uno.png)

## Camera and face detection

We used the OpenMV camera to run a Haar-cascade frontal-face detector. When a face was detected, the program set an output pin to activate an LED and an alarm.

The [face_detect.py](software/openmv/face_detect.py) file in this repository is a reconstructed example based on the project documentation. It is not the original source code used by the team.

The camera feature was designed for frontal-face detection; it was not a general-purpose object detector.

## Flight testing and improvements

We carried out several flight tests and made changes after encountering problems.

| Test | What happened | What we changed |
|---|---|---|
| Initial stability test | The drone completed a stable flight and landing during the test. | We continued with further testing. |
| Altitude test | The report records that the drone reached approximately 70 metres before losing orientation and crashing. | We repaired the damaged parts and used different colours on the front and rear arms to make the drone's direction easier to identify. |
| Further flight test | The drone was reported to be stable and responsive, but crashed during landing. | We worked on a revised frame design known as “Blue Beetle”. |

| Initial test | Damage after a test | Revised printed frame |
|---|---|---|
| ![Flight test](images/flight-test-1-stability.png) | ![Crash damage](images/flight-test-2-crash-damage.png) | ![Blue Beetle printed frame](images/blue-beetle-printed-frame.png) |

More detail is available in the [flight-test results](results/flight-test-results.md).

## Challenges and what I learned

The project gave me practical experience of taking a design from CAD modelling to a physical prototype. We had to deal with frame damage, flight-orientation problems, component integration and the limitations of the first design.

One important lesson was that a design that looks suitable in CAD still needs to be tested under real conditions. The flight tests helped us identify areas that needed improvement, particularly the visibility of the drone's orientation and the protection of its components.

## Project report and files

The [full project report](report/README.md) contains the academic documentation, design work, analysis and test observations.

The repository also contains selected project images and analysis results. The original editable CAD models and manufacturing drawings are not currently included. The [design folder](design/README.md) explains which files belong with this project.

## Notes

- This was a group project completed by four students.
- The report's objectives mention carbon-fibre filament, while the prototype described in the report was printed in PLA.
- The component descriptions identify the motion sensor as an MPU6050. One section of the report refers to it as “MPU6040”.
- The camera feature was frontal-face detection, rather than general object detection.
- The ₦430,900 project cost is the figure stated in the report. Some entries in the cost breakdown do not match their quantities or unit prices.
- Flight-test observations on this page are taken from the project report.

## Tools and technologies

SolidWorks · AutoCAD · PLA 3D printing · Arduino Uno · OpenMV IDE · Python
