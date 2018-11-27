#!/bin/bash

PGM=`basename $0`
SCRIPT_DIR=$(cd $(dirname $0); pwd)

if [ `id -u` != 0 ]
then
    echo -e "$PGM needs to be run as root."
    exit 1
fi

echo "installing..."

[ $(raspi-config nonint get_i2c) -eq "1" ] && raspi-config nonint do_i2c 0

apt-get install -y python3 python3-pip
apt-get install -y python3-touchphat
pip3 install -r ${SCRIPT_DIR}/requirements.txt

echo "done."
exit 0
