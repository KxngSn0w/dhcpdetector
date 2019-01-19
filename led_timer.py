!#/usr/bin/env python

import RPi.GPIO as GPIO
import time

# Hides GPIO Errors
GPIO.setwarnings(False)

# Sets Common GPIO Mode
GPIO.setmode(GPIO.BCM)

# Sets Pin 17 for Output
GPIO.setup(17, GPIO.OUT)

while True:
    on = GPIO.input(17)
    if on:
        time.sleep(300)
        GPIO.output(17, False)
    time.sleep(60)
