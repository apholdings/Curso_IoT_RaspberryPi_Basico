import RPi.GPIO as GPIO
import time

try:
    # Use GPIO numbering
    GPIO.setmode(GPIO.BCM)

    # Set GPIO18 as output
    GPIO.setup(17, GPIO.OUT)

    # Turn LED on
    GPIO.output(17, GPIO.HIGH)

    # Wait for one second
    time.sleep(10)

    # Turn LED Off
    GPIO.output(17, GPIO.LOW)

    # Clean up on Ctrl+C exit
    GPIO.cleanup()

except KeyboardInterrupt:
    # Clean up on Ctrl+C exit
    # Turn LED OFF
    GPIO.output(17, GPIO.LOW)
    GPIO.cleanup()