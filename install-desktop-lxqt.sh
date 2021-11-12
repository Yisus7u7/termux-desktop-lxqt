#!/bin/bash

clear
cd $HOME
#
echo -e "Installing ... "
sleep 3
pkg install python
python -m pip install --upgrade pip
pip install colorama
python termux-desktop-lxqt/lxqt.py
#
exit
