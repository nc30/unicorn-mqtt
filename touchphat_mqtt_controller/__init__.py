# coding: utf-8

import touchphat
import os
import time
from threading import Lock

from .mqtt import client, start

TARGET_NAME = os.environ.get('MQTT_TARGET_NAME')
TOPIC = 'cmnd/' + TARGET_NAME + '/display/change'

lock = Lock()

def animation():
    touchphat.all_off()
    for i in range(1, 7):
        touchphat.led_on(i)
        time.sleep(0.05)
    for i in range(1, 7):
        touchphat.led_off(i)
        time.sleep(0.05)

def blink(key):
    touchphat.all_off()
    for i in range(0, 3):
        touchphat.led_off(key)
        time.sleep(0.1)
        touchphat.led_on(key)
        time.sleep(0.1)
    touchphat.all_off()

def beep(key):
    touchphat.all_off()
    touchphat.led_on(key)
    time.sleep(0.9)
    touchphat.all_off()


@touchphat.on_release(['Back','A', 'B', 'C', 'D','Enter'])
def handle_touch(event):
    with lock:
        code = None
        if event.name == 'A':
            code = 'clock'
        if event.name == 'B':
            code = 'weather'

        if code is not None:
            client.publish(
                    topic=TOPIC,
                    payload=code
                )
            blink(event.name)

        else:
            beep(event.name)

def main():
    animation()
    start()
