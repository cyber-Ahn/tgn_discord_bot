tgn_discord_bot
---------------------------

|Build Status|  |Python versions|

Bot for Discord with some commands,chat filter, chat AI and music-bot(youtube/soundcloud) with playlist for each user in the Server 

spotify comning soon!!

Instalation and start:

install libs:

* pip3 install discord.py==0.16.12

* pip3 install discord.py==0.16.12[voice]

* pip3 install ChatterBot==0.8.7

* pip3 install chatterbot-corpus==1.1.4

* sudo pip3 install FFmpeg==1.4

* sudo pip3 install youtube_dl==2019.7.16

* sudo pip3 install spotipy==2.4.4



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

prefix admin addchatfilter word - add word to chat-filter

prefix admin rmchatfilter word - remove word from chat-filter

prefix admin kick name - kick a member

prefix admin ban name - ban a member

prefix admin unban name - unban a member

prefix admin name nickname - change nickname from member

prefix cat - shows random cat image

prefix bot - texting with the bot (bot hello / bot dice - roll the dice /bot oracle Question - answer with yes,no or maybe / 
bot bitcoin - get the Exchange rate / bot write somthing - talk with the bot)

default prefix is . example .cat

Role System:

lvl1 = .bot, .cat, .help .info commands / lvl2 = .music commands / lvl3 = .clear commands / lvl4 = .admin, .autorole commands

.admin getpermsrole level (example: .admin getpermsrole lvl2) - show all roles for level 2

.admin addpermsrole level rolename (example: .admin addpermsrole lvl2 test) - add role 'test' to level 2

.admin rmpermsrole level rolename (example: .admin rmpermsrole lvl2 test) - remove role 'test' from level 2

Music Commands:

.music join - join your voice channel

.music disconnect - disconnect voice channel

.music play url/name - plays the youtube/soundcloud-url or song from name(only youtube)

.music pause - pause the player

.music resume - resume to music

.music stop - stop the player

.music volume 50 - set volume to 50% (steps: 0, 10, 20 ... , 200)

.music addplaylist playlistname url - adds a url to playlistname

.music rmplaylist playlistname url - remove a url from playlistname

.music removeplaylsit playlistname - removes the playlist with playlistname

.music startplaylist playlistname - starts the playlist with the name playlistname

.music skip - skip to next song in playlist

.music getplaylist - shows all playlist for this server


.. ..

.. |Build Status| image:: https://caworks-sl.de/images/build.png
   :target: https://caworks-sl.de
.. |Python versions| image:: https://caworks-sl.de/images/python.png
   :target: https://caworks-sl.de
