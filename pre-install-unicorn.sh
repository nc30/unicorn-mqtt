#!/bin/bash

PGM=`basename $0`
SCRIPT_DIR=$(cd $(dirname $0); pwd)
UNICORNHATHD_ARCHIVE=https://github.com/pimoroni/unicorn-hat-hd/archive/master.zip
ICON_DIR=${SCRIPT_DIR}/unicorn_mqtt_display/display/weather-icons

if [ `id -u` != 0 ]
then
    echo -e "$PGM needs to be run as root."
    exit 1
fi

echo "installing..."

[ $(raspi-config nonint get_spi) -eq "1" ] && raspi-config nonint do_spi 0

apt-get install -y python3 python3-pip
apt-get install -y python3-pil python3-unicornhathd
apt-get install -y ttf-dejavu fonts-takao

pip3 install -r ${SCRIPT_DIR}/requirements.txt

if [ ! -e ${ICON_DIR} ]; then
    echo "nothing icon dir. get it."

    tmpdir=$(mktemp -d)
    cd ${tmpdir}
    wget -O archive.zip ${UNICORNHATHD_ARCHIVE}
    unzip archive.zip

    cd unicorn-hat-hd-master/examples/
    cp -r weather-icons ${ICON_DIR}

    rm -rf ${tmpdir}
fi

echo "done."
exit 0
