import paho.mqtt.client as mqtt
import time
import random

# MQTT broker settings
broker = "localhost"
port = 1883
topic = "sensor/temperature"

# Initialize the MQTT client
client = mqtt.Client("TemperaturePublisher")

# Connect to the MQTT broker
client.connect(broker, port)

# Function to simulate and publish temperature data
def publish_temperature_data():
    for i in range(100):
        # Simulate temperature
        temperature = round(random.uniform(24.0, 25.0), 2)
        message = f"Temperature: {temperature}°C"
        client.publish(topic, message)
        # print(f"Published: {message}")
        time.sleep(0.5)

# Publish temperature data
publish_temperature_data()

# Disconnect from the broker
client.disconnect()