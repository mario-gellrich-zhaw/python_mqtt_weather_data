"""Fetch and print the most recent air temperature from the Zurich open data API."""
import time

import requests

API_URL = (
    "https://tecdottir.herokuapp.com/measurements/tiefenbrunnen"
    "?sort=timestamp_cet%20desc&limit=5"
)


def get_most_recent_air_temperature():
    """Return the most recent air temperature reading, or None if unavailable."""
    response = requests.get(API_URL, timeout=10)
    data = response.json()

    if data["ok"] and len(data["result"]) > 0:
        # Assuming the most recent entry is the first in the sorted list
        most_recent_entry = data["result"][0]
        temperature = most_recent_entry["values"]["air_temperature"]["value"]
        return temperature

    return None


while True:
    air_temperature = get_most_recent_air_temperature()
    if air_temperature is not None:
        print(f"Publish air temperature: {air_temperature}°C")
    else:
        print("No data available.")

    time.sleep(1)
