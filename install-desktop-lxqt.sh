#!/bin/bash

clear 

#this script will configure a graphical user interface 
#(lxqt) in termux
#creator: @Yisus7u7v

echo -e """

\e[1;33mTermux Desktop\e[1m 
   \e[1;31mby \e[4;36mYisus7u7\e[4m \e[1m


"""

cd $HOME

echo -e '\e[1;36m installing lxqt and basic apps...\e[1m'

pkg update && pkg upgrade 

pkg install -y x11-repo

pkg install -y xcompmgr audacious vim-gtk qt5-qtbase-gtk-platformtheme qt5-qttools qt5-qtx11extras lxqt lxqt-build-tools otter-browser qgit featherpad gtk2 gtk3 python-tkinter tigervnc xorg-xhost openbox geany qt5-qtwebsockets qt5-qtxmlpatterns qt5-qtdeclarative 

#setting desktop and folders

mv $HOME/.config $HOME/config.old
mv $HOME/.local $HOME/.local.old 
rm -rf $HOME/.config 
rm -rf $HOME/.local
rm -rf $HOME/.themes
rm -rf $HOME/.icons
rm -rf $HOME/.vnc

cp -rf $HOME/termux-desktop-lxqt/.config $HOME
cp -rf $HOME/termux-desktop-lxqt/.local $HOME
cp -rf $HOME/termux-desktop-lxqt/backgrounds $HOME
cp -rf $HOME/termux-desktop-lxqt/.vnc $HOME
cp -rf $HOME/termux-desktop-lxqt/start-desktop $PREFIX/bin
cp -rf $HOME/termux-desktop-lxqt/stop-desktop $PREFIX/bin
cp -rf $HOME/termux-desktop-lxqt/vnc-config $PREFIX/bin

mkdir $HOME/Desktop 
mkdir $HOME/Downloads 
mkdir $HOME/Templates 
mkdir $HOME/Public 
mkdir $HOME/Documents 
mkdir $HOME/Pictures 
mkdir $HOME/Video

termux-setup-storage
ln -s $HOME/storage/music $HOME/Music


echo -e """\e[1;32menjoy!!
To Start The Vnc Server, Type start-desktop
To Stop It, Type stop-desktop
or You Can Manually Type vncserver , vncserver -kill
\e[1m"""

exit
