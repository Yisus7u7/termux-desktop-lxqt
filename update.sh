#!/bin/bash
#script for update lxqt desktop
apt update
apt install xfce4-settings
rm -rf $HOME/.config.old
rm -rf $HOME/.icons
rm -rf $HOME/.themes
rm -rf $HOME/.local
mv $HOME/.config $HOME/.config.old
git pull $HOME/termux-desktop-lxqt/
#setting themes and icons
cp -rf $HOME/termux-desktop-lxqt/icons.tar $HOME
cp -rf $HOME/termux-desktop-lxqt/themes.tar $HOME
tar -xvf $HOME/icons.tar 
tar -xvf $HOME/themes.tar
rm -rf $HOME/icons.tar
rm -rf $HOME/themes.tar
cp -rf $HOME/termux-desktop-lxqt/.config $HOME
cp -rf $HOME/termux-desktop-lxqt/.local $HOME
