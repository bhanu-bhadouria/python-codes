import time
import paho.mqtt.client as paho
#import Adafruit_DHT as dht 

#broker="broker.hivemq.com"
#broker="172.16.180.240"
#broker=“mqtt.eclipse.org“
broker = "test.mosquitto.org"

def on_connect(client2, userdata, flags, rc):
    print("Publisher Connected with result code "+str(rc))
    time.sleep(2)

#define DHT11 reading
# def DHT11_data():
# 	# Sensor data of temperature and humidity
# 	humi, temp = dht.read_retry(11,4) 
# # 	return humi, temp

client2= paho.Client("client-02")
print("Connecting to broker...",broker)
client2.connect(broker)
client2.on_connect = on_connect

client2.loop_start()

try:
    while True:
        for i in range(10,50):
            print("publishing...",i)
            client2.publish("mit/temperature",str(i))
            time.sleep(10)
               
except KeyboardInterrupt:
    client2.loop_stop()
    client2.disconnect() 