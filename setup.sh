#!/bin/bash
#title:          tgn_discord_bot
#description:    Bot for Discord with some commands and chat AI
#author:         cyber Ahn
#date:           20181220
#version:        1.0
#usage:          sudo bash setup.sh
#Support:        http:caworks-sl.de/TGN
#OS:             Debian_Stretch_Raspbian_2018.07 / Python3.5 !!!
#==============================================================================

echo -e "\e[32m#######################################################"
echo -e "\e[32m####      \e[31mtgn_discord_bot INSTALLATION FOR           \e[32m###"
echo -e "\e[32m####           \e[31mRASPBERRY PI 3 & PI 3 B+             \e[32m###"
echo -e "\e[32m####               \e[33mby cyber Ahn                     \e[32m###"
echo -e "\e[32m####           \e[34mhttp://caworks-sl.de                 \e[32m###"
echo -e "\e[32m#######################################################"

sudo apt-get update

echo -e "\n\e[33m>> \e[31mSetup Clock (y/n)?\e[32m"
read answer
if [ "$answer" != "${answer#[Yy]}" ] ;then
dpkg-reconfigure tzdata
cat /etc/localtime
sudo apt-get -y install ntp
sudo apt-get -y install ntpdate
ntpd -qg
sleep 3
fi

clear

echo -e "\e[33m>> \e[31mInstall Remote Desktop (y/n)?\e[32m"
read answer
if [ "$answer" != "${answer#[Yy]}" ] ;then
sudo apt-get -y install xrdp
sleep 5
clear
fi

echo -e "\e[33m>> \e[31mDownload Libs\e[32m"
sudo python3 -m pip install -U discord.py
sudo python3 -m pip install -U discord.py[voice]
sudo pip3 install chatterbot
sleep 5

clear

echo -e "\e[33m>> \e[31mInstall Java (y/n)?\e[32m"
read answer
if [ "$answer" != "${answer#[Yy]}" ] ;then
sudo mkdir /usr/java
cd /usr/java
wget http://www.caworks-sl.de/data/download/jdk-8u162-linux-arm32-vfp-hflt.tar.gz
sudo tar xf jdk-8u162-linux-arm32-vfp-hflt.tar.gz
sudo update-alternatives --install /usr/bin/java java /usr/java/jdk1.8.0_162/bin/java 1000
sudo update-alternatives --install /usr/bin/javac javac /usr/java/jdk1.8.0_162/bin/javac 1000
java -version
sleep 3
clear

echo -e "\e[31m\e[7m>>\e[0m \e[33mReboot System in 10 sec \e[31m\e[7m<<\e[0m"
sleep 10
reboot
