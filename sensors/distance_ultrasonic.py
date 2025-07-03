import RPi.GPIO as GPIO
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from log_event import log_event

TRIG_PIN = 23
ECHO_PIN = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def get_distance():
    # Send 10µs pulse to TRIG
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    # Wait for echo start
    start_time = time.time()
    while GPIO.input(ECHO_PIN) == 0:
        start_time = time.time()

    # Wait for echo end
    stop_time = time.time()
    while GPIO.input(ECHO_PIN) == 1:
        stop_time = time.time()

    elapsed = stop_time - start_time
    distance_cm = (elapsed * 34300) / 2
    return distance_cm

print("Ultrasonic distance measurement started (Ctrl+C to exit)")

try:
    while True:
        dist = get_distance()
        print(f"📏 Distance: {dist:.2f} cm")
        time.sleep(1)
	log_event("distance", round(dist, 2), "Ultrasonic")
except KeyboardInterrupt:
    print("Exiting.")
    GPIO.cleanup()
