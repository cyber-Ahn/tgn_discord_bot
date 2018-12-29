# tgn_discord_bot
Bot for Discord with some commands,chat filter, chat AI and music-bot with playlist for each user in the Server 


Instalation and start:

install libs:

* sudo python3 -m pip install -U discord.py

* sudo python3 -m pip install -U discord.py[voice]

* sudo pip3 install chatterbot

* sudo pip3 install FFmpeg

* sudo python3 -m pip install -U youtube_dl



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

Commands:

prefix autorole rolename - set role for new members (.autorole Member)

prefix autorole clear - delete the role for new members

prefix music help - commands for the music bot

prefix clear 5 - delete last 5 messages in channel

prefix admin role role_name name - add role to member

prefix admin removerole role_name name - remove role from member

prefix admin kick name - kick a member

prefix admin ban name - ban a member

prefix admin unban name - unban a member

prefix admin name nickname - change nickname from member

prefix cat - shows random cat image

prefix bot - texting with the bot (bot hello / bot dice - roll the dice /bot oracle Question - answer with yes,no or maybe / 
bot bitcoin - get the Exchange rate / bot write somthing - talk with the bot)

default prefix is . example .cat

Music Commands:

.music join - join your voice channel

.music disconnect - disconnect voice channel

.music play url - plays the youtube url

.music search name of song - search a song on youtube and play this song

.music pause - pause the player

.music resume - resume to music

.music stop - stop the player

.music addplaylist playlistname url - adds a url to playlistname

.music rmplaylist playlistname url - remove a url from playlistname

.music removeplaylsit playlistname - removes the playlist with playlistname

.music startplaylist playlistname - starts the playlist with the name playlistname

.music skip - skip to next song in playlist

.music getplaylist - shows all playlist for this server
