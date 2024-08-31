import paho.mqtt.client as mqtt

# MQTT broker settings
broker = "localhost"
port = 1883
topic = "sensor/temperature"

# Callback function for when a message is received
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")

# Initialize the MQTT client
client = mqtt.Client("TemperatureSubscriber", clean_session=False)

# Set the callback function for message reception
client.on_message = on_message

# Enable logging
client.on_log = lambda client, userdata, level, buf: print(f"Log: {buf}")

# Connect to the MQTT broker
client.connect(broker, port)

# Subscribe to the temperature topic
client.subscribe(topic, qos=1)

# Start the MQTT client loop to process messages
client.loop_forever()
