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
mv termux-desktop/main.py $PREFIX/bin/e-tnv
#pkg in wget;wget https://github.com/Learn-Termux/env-distro/raw/main/e-tnv.sh;chmod +x e-tnv.sh;./e-tnv.sh
wget https://github.com/Learn-Termux/env-distro/raw/main/font.ttf -O .termux/font.ttf
termux-reload-settings
echo -e """\e[1;32menjoy!!
To Start The Vnc Server, Type e-tnv start
To Stop It, Type e-tnv stopall
or You Can Manually Type vncserver , vncserver -kill
\e[1m"""

