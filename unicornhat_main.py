#!/usr/bin/env python3
# coding: utf-8

"""
    unicornhat_mqtt_controllerを始動させるサンプル
    別途環境変数の指定が必要です。
    
    必要な環境変数は以下のとおりです。
    
    MQTT_NAME MQTT上で使用する名前
    MQTT_HOST MQTTホスト名
    MQTT_USER MQTTユーザー名
    MQTT_PASSWORD MQTTパスワード
    MQTT_PORT MQTTポート
    OPENWEATHER_API_KEY openWeatherのAPIキー
    WEATHER_CITY 天気予報を行う地域
    
 """

from logging import getLogger
logger = getLogger('unicorn_mqtt_display')

from logging import Formatter, StreamHandler, INFO
import sys
import os

logger.setLevel(INFO)
handler = StreamHandler(stream=sys.stdout)
handler.setFormatter(
    Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
)
logger.addHandler(handler)


from unicorn_mqtt_display.mqtt import start, end

if __name__ == '__main__':
    try:
        start()

    except KeyboardInterrupt:
        pass

    except Exception as e:
        logger.exception(e)
        raise e

    finally:
        logger.info('stopping...')
        end()
        sys.stdout.write("bye.\n")
