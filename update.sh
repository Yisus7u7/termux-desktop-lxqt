#!/bin/bash
#script for update lxqt desktop
cd $HOME
apt update
apt upgrade -y
rm -rf $HOME/.config.old
rm -rf $HOME/.icons
rm -rf $HOME/.themes
rm -rf $HOME/.local
mv $HOME/.config $HOME/.config.old
git pull $HOME/termux-desktop-lxqt/
#setting themes and icons
cp -rf $HOME/termux-desktop-lxqt/data.tar.xz $HOME
tar -xvf data.tar.xz
rm data.tar.xz
