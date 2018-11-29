#!/bin/bash

######################################################################
#
#  pre-install-touchphat.sh: touchphat-mqtt Touchphat側のインストールスクリプト
#  Written by Shoji Iwaura (xshell inc) at 2018/11/27
#
# Usage  : ./pre-install-touchphat.sh
#
#
######################################################################

# スクリプト名の取得
PGM=`basename $0`
# スクリプト（このファイル）の絶対パスを取得
SCRIPT_DIR=$(cd $(dirname $0); pwd)

# メッセージの出力
echo "installing..."

# i2dが有効になっていない場合、有効にする
[ $(sudo raspi-config nonint get_i2c) -eq "1" ] && sudo raspi-config nonint do_i2c 0

# 必要なaptパッケージのインストール
sudo apt-get install -y python3 python3-pip
sudo apt-get install -y python3-touchphat

# pipパッケージのインストール
sudo pip3 install -r ${SCRIPT_DIR}/requirements.txt

echo "done."
exit 0
