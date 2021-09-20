#IOT Subscriber
import paho.mqtt.client as mymqtt
import time

MQTT_SERVER = "test.mosquitto.org"
#MQTT_SERVER = "172.16.180.240"
#MQTT_SERVER="broker.hivemq.com"
#MQTT_SERVER=“mqtt.eclipse.org"

MQTT_TOPIC = "mit/temperature"
 
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_TOPIC)
 
def on_message(client, userdata, msg):
    print(msg.topic+'  '+str(msg.payload))

client = mymqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883, 60)
client.loop_start()
try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect() 