# Script created by Josephine Esposito | 01/10/2022
# The repository can be found on GitHub: @josephine-00

import time
import paho.mqtt.client as paho
from paho import mqtt

import KML
import p # I dati modificabili sono qui!

# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

# using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
# userdata is user defined data of any type, updated by user_data_set()
# client_id is the given name of the client
client = paho.Client(client_id=p.client_id, userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

# enable TLS for secure connection
# client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)      # not enables on the test MQTT mosquitto broker
# set username and password
client.username_pw_set(p.username, p.password)
# connecting to mosquitto on port 1883 (default for MQTT)
client.connect(p.host, p.port)

# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

# subscribe to all topics of encyclopedia by using the wildcard "#"
client.subscribe("KML_testVS/#", qos=1)

# a single publish, this can also be done in loops, etc.
##client.publish("KML_testVS/KML", payload="hot", qos=0)  # receives the payload(array of bytes) from the original py programm!!

# loop_forever for simplicity, here you need to stop the loop manually
# you can also use loop_start and loop_stop

messagekml = KML.kml_parser()

for i in range(len(messagekml)):
    while client.loop() == 0:
        client.publish("KML_testVS/KML", payload=messagekml[i], qos=0)
        time.sleep(p.wait)          # it will sleep for 30 seconds before next call

#original
#client.loop_forever()