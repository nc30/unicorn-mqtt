#!/bin/bash

######################################################################
#
#  pre-install-unicorn.sh: unicorn-mqtt UnicornHatHD側のインストールスクリプト
#  Written by Shoji Iwaura (xshell inc) at 2018/11/27
#
# Usage  : ./pre-install-unicorn.sh
#
#
######################################################################

# スクリプト名の取得
PGM=`basename $0`
# スクリプト（このファイル）の絶対パスを取得
SCRIPT_DIR=$(cd $(dirname $0); pwd)

# 公式リポジトリのzipURL
UNICORNHATHD_ARCHIVE=https://github.com/pimoroni/unicorn-hat-hd/archive/master.zip
# 公式アイコンのファイル格納先
ICON_DIR=${SCRIPT_DIR}/unicorn_mqtt_display/display/weather-icons


# メッセージの出力
echo "installing..."

# spiが有効になっていない場合、有効にする
[ $(sudo raspi-config nonint get_spi) -eq "1" ] && sudo raspi-config nonint do_spi 0

# 必要なaptパッケージのインストール
sudo apt-get install -y python3 python3-pip
sudo apt-get install -y python3-pil python3-unicornhathd
sudo apt-get install -y ttf-dejavu fonts-takao

# pipパッケージのインストール
sudo pip3 install -r ${SCRIPT_DIR}/requirements.txt

# 天気アイコンが必要な場合、これを作成する。
if [ ! -e ${ICON_DIR} ]; then
    echo "nothing icon dir. get it."

    # mktempコマンドで一時的に使用するディレクトリを作成する
    tmpdir=$(mktemp -d)
    cd ${tmpdir}
    
    # アーカイブのダウンロード
    # -O オプションでファイル名を指定する。これをすることにより大元のファイル名が変わった場合でも対応できる。
    wget -O archive.zip ${UNICORNHATHD_ARCHIVE}
    unzip archive.zip

    # ファイルのコピー作業
    cd unicorn-hat-hd-master/examples/
    cp -rv weather-icons ${ICON_DIR}

    # 一時ディレクトリの削除
    cd ${SCRIPT_DIR}    
    rm -rf ${tmpdir}
fi

echo "done."
exit 0
