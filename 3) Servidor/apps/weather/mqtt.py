# mqtt.py

import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("mqtt", 1883, 60)  # connect to your broker

def publish(topic, message):
    client.publish(topic, message)  # publish a message