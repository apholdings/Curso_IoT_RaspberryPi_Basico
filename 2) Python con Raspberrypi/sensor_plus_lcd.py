import Adafruit_DHT
from RPi_GPIO_i2c_LCD import lcd
from time import sleep

# Sensor type
DHT_SENSOR = Adafruit_DHT.DHT11

LCD = lcd.HD44780(0x27)

# GPIO pin the sensor is connected to
GPIO_PIN = 17

# Try to grab a sensor reading
humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, GPIO_PIN)

if humidity is not None and temperature is not None:
    while True:
        LCD.backlight("on")
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
        LCD.set(f"Temp: {str(temperature)} {chr(223)} C",1)
        LCD.set(f"Humidity: {str(humidity)} %",2)
        sleep(1)
else:
    print("Failed to retrieve data from sensor")

