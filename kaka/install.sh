#! /bin/bash

mkdir /opt/kaka
cp -r . /opt/kaka/
ln -s /opt/kaka/play.py /bin/play.py
./bootstrap.sh
