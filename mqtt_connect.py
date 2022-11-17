import paho.mqtt.client as mqtt
import settings

client = mqtt.Client("led-monitor-client")

def send_led_status(status):
    client.connect(host=settings.mqtt_broker, port=settings.mqtt_port)
    print("Publishing message to ESP8266/LED: {}".format(status))
    client.publish("ESP8266/LED", status)
    client.disconnect()