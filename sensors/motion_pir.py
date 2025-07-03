import RPi.GPIO as GPIO
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from log_event import log_event

PIR_PIN = 17  # GPIO pin where OUT from PIR is connected

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

print("PIR motion detection started (Ctrl+C to exit)")

try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion Detected!")
	    log_event("motion", 1, "PIR")
        else:
            print("No motion.")
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting.")
    GPIO.cleanup()
