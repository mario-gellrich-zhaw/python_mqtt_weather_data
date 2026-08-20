"""Subscribe to an MQTT topic and print incoming temperature readings."""
import paho.mqtt.client as mqtt

# MQTT broker settings
BROKER = "localhost"
PORT = 1883
TOPIC = "sensor/temp"

# Callback function for when a message is received
def on_message(_client, _userdata, message):
    """Print the temperature carried by an incoming MQTT message."""
    payload = message.payload.decode()
    try:
        temperature = float(payload)
        print(f"Received temperature: {temperature}°C")
    except ValueError:
        pass

# Initialize the MQTT client
client = mqtt.Client("Subscriber")

# Set the callback function for message reception
client.on_message = on_message

# Enable logging (optional)
# client.on_log = lambda client, userdata, level, buf: print(f"Log: {buf}")

# Connect to the MQTT broker
client.connect(BROKER, PORT)

# Subscribe to the topic
client.subscribe(TOPIC)

# Start the MQTT client loop to process messages
client.loop_forever()
