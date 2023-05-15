from django.db import models

# Create your models here.
class DHT11SensorData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Temperature: {self.temperature}, Humidity: {self.humidity} at {self.timestamp}'