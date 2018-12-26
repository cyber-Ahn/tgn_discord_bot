# tgn_discord_bot
Bot for Discord with some commands,chat filter and chat AI

music option cominf soon

Instalation and start:

install libs:

* sudo python3 -m pip install -U discord.py

* sudo python3 -m pip install -U discord.py[voice]

* sudo pip3 install chatterbot



- git clone https://github.com/cyber-Ahn/tgn_discord_bot.git

- cd tgn_discord_bot



get a tokken from https://discordapp.com/developers/applications

change tokken in /SETTINGS/SECRETS.py


- sudo nano /SETTINGS/SECRETS.py


edit /SETTINGS/authorization.json

and change the roles for authorization to some commands

- sudo nano /SETTINGS/authorization.json

start bot with: 

- python3 bot.py

add to autostart:

- sudo nano /home/pi/.config/lxsession/LXDE-pi/autostart
  or
- sudo nano  /etc/xdg/lxsession/LXDE-pi/autostart

after LXDE-pi add line:

- @lxterminal -e /home/pi/tgn_discord_bot/start_bot.sh

add bot to your server

to get all commands write in discord: *help
