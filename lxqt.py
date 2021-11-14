#!/data/data/com.termux/files/usr/bin/python

#
from os import system
from time import sleep
from colorama import *
import os
#
init(autoreset=True)
#
RED         = Fore.RED
GREEN       = Fore.GREEN
BLUE        = Fore.BLUE
YELLOW      = Fore.YELLOW
MAGENTA     = Fore.MAGENTA
CYAN        = Fore.CYAN

BOLD        = '\033[1m'
BRIGHT      = Style.BRIGHT

BACKRED     = Back.RED
BACKGREEN   = Back.GREEN
BACKYELLOW  = Back.YELLOW
BACKMAGENTA = Back.MAGENTA

RESET      = Style.RESET_ALL
#

class pkgs:
	X11      = 'pkg install -y x11-repo'
	PKGS     = 'pkg install -y xcompmgr audacious xpdf qt5-qtbase-gtk-platformtheme qt5-qttools qt5-qtx11extras lxqt lxqt-build-tools otter-browser qgit featherpad gtk2 gtk3 python-tkinter tigervnc xorg-xhost openbox geany qt5-qtwebsockets qt5-qtxmlpatterns qt5-qtdeclarative termux-api geany-plugins xorg-xprop neofetch galculator qt5-qttools glade feathernotes xorg-xprop mtpaint xorg-xhost'
	UNSTABLE = 'pkg install -y gobject-introspection at-spi2-atk '
	

def icons():
	system('wget https://github.com/Yisus7u7/termux-desktop-lxqt/releases/download/data/termux_desktop_lxqt_data.tar.xz')
	system('tar -xvf termux_desktop_lxqt_data.tar.xz')
	system('rm termux_desktop_lxqt_data.tar.xz')
	
def themes():
	system('mv materia-theme/* $PREFIX/share/themes/')
	system('rm -rf materia-theme')
	system('wget https://github.com/Yisus7u7/termux-desktop-lxqt/releases/download/data/breeze-cursor-theme_5.20.5-4_all.deb')
	system('apt install ./breeze-cursor-theme_5.20.5-4_all.deb')
	system('rm breeze-cursor-theme_5.20.5-4_all.deb')

class extra:
	def access_storage():
		system('termux-setup-storage')

	def symbolic_link():
		system('ln -s $HOME/storage/music $HOME/Music')
#	
def setting_desktop():
	system('mv $HOME/.config $HOME/.config.old')
	system('mv $HOME/.local $HOME/.local.old ')
	system('rm -rf $HOME/.config ')
	system('rm -rf $HOME/.local')
	system('rm -rf $HOME/.themes')
	system('rm -rf $HOME/.icons')
	system('rm -rf $HOME/.vnc')
	system('rm -rf $HOME/Pictures')
	system('rm $PREFIX/bin/start-desktop')
	system('rm $PREFIX/bin/stop-desktop')
	system('rm $PREFIX/bin/vnc-config')
	system('rm $PREFIX/bin/vnc-autostart-config')
	system('cp -rf $HOME/termux-desktop-lxqt/start-desktop $PREFIX/bin')
	system('cp -rf $HOME/termux-desktop-lxqt/stop-desktop $PREFIX/bin')
	system('cp -rf $HOME/termux-desktop-lxqt/vnc-config $PREFIX/bin')
	system('cp -rf $HOME/termux-desktop-lxqt/vnc-autostart-config $PREFIX/bin')

def folders():
	system('mkdir $HOME/Desktop')
	system('mkdir $HOME/Downloads')
	system('mkdir $HOME/Templates')
	system('mkdir $HOME/Public')
	system('mkdir $HOME/Documents')
	system('mkdir $HOME/Video')
	system('chmod +x ~/.vnc/xstartup')
	
def exit_py():
	pass
#

def main():
	pass

os.chdir(r'/data/data/com.termux/files/home')
interface = BRIGHT + MAGENTA + "Termux-Desktop "
print(interface.center(60))
sleep(1)
print(BRIGHT + MAGENTA + "  ENVIRONMENT :" + RESET + BRIGHT + CYAN + " LXQT ")
sleep(0.2)
print(BRIGHT + MAGENTA + "  VERSION     :" + RESET + BRIGHT + GREEN + " 2.1.3 ")
sleep(0.2)
print(BRIGHT + MAGENTA + "  CREATED BY  :" + RESET + BRIGHT + YELLOW + " Yisus7u7")
sleep(1)
print(BRIGHT + MAGENTA + "\n\t Push " + BRIGHT + YELLOW + "ENTER " + BRIGHT + MAGENTA + "to continue ... ")
input(BRIGHT + GREEN + " >> ")


print(BRIGHT + MAGENTA + "REMOVING OLD FILES IF EXISTS" + RESET)
setting_desktop()

print(BRIGHT + MAGENTA + "REMOVING UNNECESSARY FILES AND CLEARING CACHE")
system('apt clean')
system('apt autoremove')

print(RESET + BRIGHT + MAGENTA + "INSTALLING PACKAGES AND APPLICATIONS " + BRIGHT + GREEN )
sleep(0.5)
system(pkgs.X11)
system(pkgs.PKGS)
system(pkgs.UNSTABLE)

print(RESET + BRIGHT + MAGENTA + " \tFetching Themes and Icon File ")
sleep(0.5)
icons()
themes()

print(RESET + MAGENTA + "\t  Settingup Directories")
sleep(0.5)
folders()

print(RESET + BRIGHT + MAGENTA + "\t Almost Done ...")
sleep(0.2)
extra.access_storage()
extra.symbolic_link()

print(RESET + BRIGHT + MAGENTA + "\tPROCESS FINISHED ")
sleep(0.5)

print(RESET + BRIGHT + GREEN + " If You Facing Any Issues About LXQT Post at : ")
print(RESET + BRIGHT + BACKMAGENTA + " https://github.com/Yisus7u7/termux-desktop-lxqt/issues ")
sleep(1)
