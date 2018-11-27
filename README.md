# unicorn-mqtt

MQTT通信を使い、TouchPhatを刺したRaspberryPiでUnicornHatHDを刺したRaspberryPiの表示を制御するサンプル。


## 概要

このスクリプトはMQTT通信を用いてTouchPhatのボタン操作でUnicornHatHDの表示を時計、天気予報と切り替え動作を行うサンプルです。

MQTTブローカーは別途用意する必要がありますが、CoudMQTTサービスを使うことを推奨します。
https://www.cloudmqtt.com



## 環境構築
それぞれ以下のコマンドを使用して必須パッケージをインストールします。
インストールスクリプトを使用するか、マニュアルで設定します。

### UnicornHatHD側

#### スクリプトを使用する場合

```shell
$ sudo pre-install-unicorn.sh
```

#### 手動で行う場合

```shell
$ sudo raspi-config # SPIを有効にする
$ sudo apt-get install python3-pip python3-dev python3-spidev python3-pil python3-numpy -y
$ sudo apt-get install ttf-dejavu fonts-takao -y
$ sudo pip3 install unicornhathd paho-mqtt requests
```

ライブラリ内の ``` unicorn_mqtt_display/display ``` ディレクトリ上に公式ライブラリの ``` examples ``` 上にある
``` weather-icons ```　ディレクトリをコピーする必要があります 

https://github.com/pimoroni/unicorn-hat-hd/tree/master/examples/



### TouchPhat側

#### スクリプトを使用する場合

```shell
$ sudo pre-install-touchphat.sh
```

#### 手動で行う場合

```shell
$ sudo raspi-config # I2Cを有効にする
$ sudo apt-get install python3-pip python3-dev python3-smbus -y
$ sudo pip3 install touchphat paho-mqtt
```


## 起動コマンド
これらの起動はそれぞれ下記のようなコマンドを使ってください。

### touchphat_main側

```shell
$ MQTT_TARGET_NAME=nagoya \
MQTT_NAME=matsumoto \
MQTT_HOST={mqtt broker hostname} \
MQTT_USER={mqtt user} \
MQTT_PASSWORD={mqtt password} \
MQTT_PORT={mqtt port} \
python3 touchphat_main.py
```


### unicornhat_main側
```shell
$ MQTT_NAME=nagoya \
MQTT_HOST={mqtt broker hostname} \
MQTT_USER={mqtt user} \
MQTT_PASSWORD={mqtt password} \
MQTT_PORT={mqtt port} \
OPENWEATHER_API_KEY={openWeather api key} \
WEATHER_CITY={天気予報を行う地域} \
python3 unicornhat_main.py
```



## ライブラリへのリンク

- CloudMQTT - https://www.cloudmqtt.com
- UnicornHatHD - https://github.com/pimoroni/unicorn-hat-hd
- touchPhat - https://github.com/pimoroni/touch-phat
- paho.mqtt - https://www.eclipse.org/paho/clients/python/docs/
- openWeather - https://openweathermap.org/api
- requests - https://requests-docs-ja.readthedocs.io/en/latest/
