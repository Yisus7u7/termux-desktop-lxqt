#!/bin/bash

clear
cd $HOME
#
echo -e "Installing ... "
sleep 1
pkg install python wget -y
python -m pip install --upgrade pip
pip install colorama
clear
python termux-desktop-lxqt/lxqt.py
chmod +x termux-desktop-lxqt/main.py
mv termux-desktop-lxqt/main.py $PREFIX/bin/e-tnv
echo -e """\e[1;32menjoy!!
To Start The Vnc Server, Type e-tnv start
To Stop It, Type e-tnv stopall
or You Can Manually Type vncserver , vncserver -kill
\e[1m"""

