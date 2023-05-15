import Adafruit_DHT
import time
import requests

# Sensor type
DHT_SENSOR = Adafruit_DHT.DHT11

# GPIO pin the sensor is connected to
GPIO_PIN = 17

# API endpoint
url = "http://backend:8000/api/weather/add"

# Time interval (in seconds)
interval = 30

while True:
    # Try to grab a sensor reading
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, GPIO_PIN)

    if humidity is not None and temperature is not None:
        # Prepare data
        data = {
            'humidity': humidity, 
            'temperature': temperature
        }
        # Try to make POST request
        try:
            response = requests.post(url, data=data)
            # If the request was successful
            if response.status_code == 200:
                print(f"Data successfully sent. Temperature: {temperature}, Humidity: {humidity}")
            else:
                print(f"Failed to send data. Response code: {response.status_code}")
        except requests.exceptions.RequestException as err:
            print(f"Failed to send data due to exception: {err}")
    
    # Wait for the next reading
    time.sleep(interval)