perm = 2

from commands import debug
from os import path
import discord
import os
import youtube_dl

players = {}

def saveFile(message, name, url):
    if not path.isdir("playlist/" + message.server.id):
        os.makedirs("playlist/" + message.server.id)
    with open("playlist/" + message.server.id + "/" + name, "a") as f:
        f.write(url+"\n")
        f.close()

def check_in_list(message, name, url):
    if not path.isdir("playlist/" + message.server.id):
        return "No"
    elif not path.isfile("playlist/" + message.server.id + "/" + name):
        return "no"
    else:
        file = open("playlist/" + message.server.id + "/" + name,"r")
        lines = file.readlines()
        file.close()
        if (url+"\n") in lines:
            return "yes"
        else:
            return "no"

def removeFile(message, name):
    if path.isfile("playlist/" + message.server.id + "/" + name):
        os.remove("playlist/" + message.server.id + "/" + name)

def removeUrl(message, name, url):
    if path.isfile("playlist/" + message.server.id + "/" + name):
        file = open("playlist/" + message.server.id + "/" + name,"r")
        lines = file.readlines()
        file.close()
        file = open("playlist/" + message.server.id + "/" + name,"w")
        for line in lines:
            if line != (url+"\n"):
                file.write(line)
        file.close()

def play_list(server, args):
    debug.write("green", "start playlist")
    

async def ex(args, message, client, invoke):
    if len(args) > 0:
        if args[0] == "join":
            channel = message.author.voice.voice_channel
            await client.join_voice_channel(channel)
            debug.write("green", "Join channel!")
            await client.send_message(message.channel, "'.music help' - for command list")
        
        
        elif args[0] == "disconnect":
            debug.write("red", "disconnect channel")
            server = message.server
            voice_client = client.voice_client_in(server)
            await voice_client.disconnect()
        
        elif args[0] == "play":
            id = message.server.id
            if id in players:
                players[id].stop()
            url = args[1]
            debug.write("green", "load and play: "+ url)
            server = message.server
            voice_client = client.voice_client_in(server)
            player = await voice_client.create_ytdl_player(url)
            players[server.id] = player
            player.start()
        
        elif args[0] == "pause":
            debug.write("green", "pause")
            id = message.server.id
            players[id].pause()
        
        elif args[0] == "stop":
            debug.write("red", "stop")
            id = message.server.id
            players[id].stop()
        
        elif args[0] == "resume":
            debug.write("green", "resume")
            id = message.server.id
            players[id].resume()

        elif args[0] == "addplaylist":
            name = args[1]
            url = args[2]
            if check_in_list(message, name, url) == "no":
                saveFile(message, name, url)
                debug.write("green", "add " + url + " to playlist " + name + " on server " + message.server.id)
                await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description=("Song add to playlist %s" % name)))
            else:
                debug.write("red", "song already exists")
                await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="song already exists"))
        
        elif args[0] == "rmplaylist":
            name = args[1]
            url = args[2]
            removeUrl(message, name, url)
            debug.write("red", "remove " + url + " from playlist: " + name)
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description=("remove %s from playlist: %s" % (url, name))))
        
        elif args[0] == "removeplaylist":
            name = args[1]
            removeFile(message, name)
            debug.write("red", "remove playlist: " + name)
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description=("remove playlist: %s" % name)))





        elif args[0] == "help":
            text = ".music join - join your voice channel\n"
            text = text + ".music disconnect - disconnect voice channel\n"
            text = text + ".music play url - plays the youtube url\n"
            text = text + ".music pause - pause the player\n"
            text = text + ".music resume - resume to music\n"
            text = text + ".music stop - stop the player\n"
            text = text + ".music addplaylist playlistname url - adds a url to playlistname\n"
            text = text + ".music rmplaylist playlistname url - remove a url from playlistname\n"
            text = text + ".music removeplaylsit playlistname - removes the playlist with playlistname\n"
            await client.send_message(message.channel, text)


    else:
        await client.send_message(message.channel, "What do you want?")
        debug.write("red", "What do you want?")