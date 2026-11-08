# Object detection on the OpenMV Cam H7 Plus (MicroPython)
# Haar-cascade face detection; an LED/alarm output switches on when a face is found.
# Reconstructed from the project report: the sensor setup lines were not shown in full,
# so they follow the report's description (HQVGA + GRAYSCALE). Check against your original file.
import sensor, time, image
import pyb
from pyb import Pin

# Reset and configure the sensor
sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.HQVGA)
sensor.skip_frames(time=2000)

# Load Haar cascade (fewer stages = faster but less accurate)
face_cascade = image.HaarCascade("frontalface", stages=25)
print(face_cascade)

# Output pin driving the LED / beacon + alarm
led = pyb.Pin("P1", Pin.OUT_PP)

clock = time.clock()

while True:
    clock.tick()
    img = sensor.snapshot()

    # Lower scale_factor detects smaller objects; higher threshold = more detections, more false positives
    objects = img.find_features(face_cascade, threshold=1.75, scale_factor=1.25)

    for r in objects:
        img.draw_rectangle(r)

    if objects:
        led.high()   # face detected: beacon on
    else:
        led.low()

    print(clock.fps())
