"""Fetch weather data from an API and publish it to an MQTT broker."""
import time

import requests
import paho.mqtt.client as mqtt

# MQTT broker settings
BROKER = "localhost"
PORT = 1883
TOPIC = "sensor/temp"

API_URL = (
    "https://tecdottir.herokuapp.com/measurements/tiefenbrunnen"
    "?sort=timestamp_cet%20desc&limit=5"
)

# Initialize the MQTT client
client = mqtt.Client("Publisher")

# Enable logging (optional)
# client.on_log = lambda client, userdata, level, buf: print(f"Log: {buf}")

# Connect to the MQTT broker
client.connect(BROKER, PORT)

# Function to fetch the most recent data from the weather API
def get_data():
    """Return the most recent air temperature reading, or None if unavailable."""
    response = requests.get(API_URL, timeout=10)
    data = response.json()

    if data["ok"] and len(data["result"]) > 0:
        # Assuming the most recent entry is the first in the sorted list
        most_recent_entry = data["result"][0]
        value = most_recent_entry["values"]["air_temperature"]["value"]
        return value

    return None

# Function to fetch and publish data
def publish_data():
    """Continuously fetch and publish temperature data until interrupted."""
    try:
        while True:
            value = get_data()
            if value is not None:
                message = str(value)
                print(f"Publishing: {message}°C from {TOPIC}")
                client.publish(TOPIC, message)
            else:
                print("No data available.")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Disconnecting from broker...")
        client.disconnect()

if __name__ == "__main__":
    # Publish data
    publish_data()
