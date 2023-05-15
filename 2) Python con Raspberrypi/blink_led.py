import RPi.GPIO as GPIO
import time

# Use GPIO numbering
GPIO.setmode(GPIO.BCM)

# Set GPIO18 as output
GPIO.setup(17, GPIO.OUT)

try:
    # Repeat forever
    while True:
        # Turn LED on
        GPIO.output(17, GPIO.HIGH)
        # Wait for one second
        time.sleep(1)
        # Turn LED off
        GPIO.output(17, GPIO.LOW)
        # Wait for one second
        time.sleep(1)
except KeyboardInterrupt:
    # Clean up on Ctrl+C exit
    GPIO.cleanup()