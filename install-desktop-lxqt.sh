#!/bin/bash

clear
cd $HOME
#
echo -e "Installing ... "
sleep 1
pkg install python wget -y
python -m pip install --upgrade pip
pip install colorama
python termux-desktop-lxqt/lxqt.py

echo -e """\e[1;32menjoy!!
To Start The Vnc Server, Type start-desktop
To Stop It, Type stop-desktop
or You Can Manually Type vncserver , vncserver -kill
\e[1m"""

