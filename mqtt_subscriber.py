import paho.mqtt.client as mqtt

# MQTT broker settings
broker = "localhost"
port = 1883
topic = "sensor/temp"

# Callback function for when a message is received
def on_message(client, userdata, message):
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
client.connect(broker, port)

# Subscribe to the topic
client.subscribe(topic)

# Start the MQTT client loop to process messages
client.loop_forever()