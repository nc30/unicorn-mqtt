# coding: utf-8

from logging import getLogger
logger = getLogger(__name__)

import paho.mqtt.client as mqtt
import os

NAME = os.environ.get('MQTT_NAME', 'mqtt_controller')
MQTT_HOST = os.environ.get('MQTT_HOST')
MQTT_USER = os.environ.get('MQTT_USER')
MQTT_PASSWORD = os.environ.get('MQTT_PASSWORD')
MQTT_PORT = int(os.environ.get('MQTT_PORT'))

client = mqtt.Client(protocol=mqtt.MQTTv311)

def on_connect(sclient, userdata, flags, respons_code):
    logger.debug('connection success.')
    client.publish('stat/' + NAME + '/status', 'connected.')


def on_disconnect(client, userdata, rc):
    logger.debug('connection disconnected. rc=%s', rc)
    if rc != 0:
        logger.error('Unexpected disconnection.')


def start():
    client.username_pw_set(MQTT_USER, password=MQTT_PASSWORD)
    client.on_disconnect = on_disconnect
    client.on_connect = on_connect

    logger.debug('connection start.')
    client.connect(MQTT_HOST, MQTT_PORT)

    logger.debug('loop start.')
    client.loop_forever()
