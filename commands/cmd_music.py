perm = 2

from commands import debug
from os import path
from urllib.parse import urlparse
from urllib import request
import urllib
import discord
import os
import time
import youtube_dl

players = {}
queues = {}

def youtube_search(keywords):
    i = 0
    ser = ""
    for x in keywords:
        if i == 1:
            ser = ser + urllib.parse.quote(x)
        elif i != 0:
            ser = ser + "+" + urllib.parse.quote(x)
        i = i + 1
    resp = request.urlopen("https://www.youtube.com/results?search_query="+ser)
    code = resp.code
    if code == 200:
        data = resp.read()
        html = data.decode("UTF-8")[:86500]
        cach = html.split('</div><div class="yt-lockup-content">')
        cach = cach[1].split('/watch?v=')
        cach = cach[1].split('" class="')
        html = cach[0]
        url = "https://www.youtube.com/watch?v="+html
        return url
    time.sleep(1)

def url_check(url):
    min_attr = ('scheme' , 'netloc')
    try:
        result = urlparse(url)
        if all([result.scheme, result.netloc]):
            return True
        else:
            return False
    except:
        return False

def youtube_check(url):
    if "www.youtube.com" in url:
        return True
    else:
        return False

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

def check_queue(id):
    if queues[id] != []:
        player = queues[id].pop(0)
        players[id] = player 
        player.start() 

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
                queues = {}
                players[id].stop()
            url = args[1]
            if url_check(url) and youtube_check(url):
                debug.write("green", "load and play: "+ url)
                server = message.server
                voice_client = client.voice_client_in(server)
                player = await voice_client.create_ytdl_player(url)
                players[server.id] = player
                player.start()
            else:
                await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Valid url! Use youtube url!"))
        
        elif args[0] == "pause":
            debug.write("green", "pause")
            id = message.server.id
            players[id].pause()
        
        elif args[0] == "stop":
            debug.write("red", "stop")
            id = message.server.id
            queues = {}
            players[id].stop()
        
        elif args[0] == "resume":
            debug.write("green", "resume")
            id = message.server.id
            players[id].resume()

        elif args[0] == "addplaylist":
            name = args[1]
            url = args[2]
            if url_check(url) and youtube_check(url):
                if check_in_list(message, name, url) == "no":
                    saveFile(message, name, url)
                    debug.write("green", "add " + url + " to playlist " + name + " on server " + message.server.id)
                    await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description=("Song add to playlist %s" % name)))
                else:
                    debug.write("red", "song already exists")
                    await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="song already exists"))
            else:
                await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Valid url! Use youtube url!"))
        
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
        
        elif args[0] == "startplaylist":
            global queues
            queues = {}
            name = args[1]
            debug.write("green", "Load playlist")
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description=("Loade Playlist: %s please wait!" % name)))
            server = message.server
            id = server.id
            if id in players:
                players[id].stop()
            voice_client = client.voice_client_in(server)
            if path.isfile("playlist/" + message.server.id + "/" + name):
                file = open("playlist/" + message.server.id + "/" + name,"r")
                lines = file.readlines()
                file.close()
            for line in lines:
                url = line.rstrip()
                player = await voice_client.create_ytdl_player(url, after= lambda: check_queue(server.id))
                if server.id in queues:
                    queues[server.id].append(player)
                else:
                    queues[server.id] = [player]
                time.sleep(1)
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description=("Loaded Playlist: %s" % name)))
            player = queues[id].pop(0)
            players[server.id] = player
            player.start()

        elif args[0] == "skip":
            debug.write("red", "skip")
            id = message.server.id
            players[id].stop()
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description="skip song!"))
        
        elif args[0] == "getplaylist":
            debug.write("green", "print all Playlists")
            file_l = ""
            for files in os.listdir("playlist/" + message.server.id):
                file_l = file_l + files + "\n"
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description=file_l))
            debug.write("yellow", file_l)
        
        elif args[0] == "search":
            debug.write("green", "search in youtube")
            url = youtube_search(args)
            debug.write("green", "url: "+url)
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description=("Load and Play: %s" % url)))
            server = message.server
            voice_client = client.voice_client_in(server)
            player = await voice_client.create_ytdl_player(url)
            players[server.id] = player
            player.start()


        elif args[0] == "help":
            text = ".music join - join your voice channel\n"
            text = text + ".music disconnect - disconnect voice channel\n"
            text = text + ".music play url - plays the youtube url\n"
            text = text + ".music search name of song - search a song on youtube and play this song\n"
            text = text + ".music pause - pause the player\n"
            text = text + ".music resume - resume to music\n"
            text = text + ".music stop - stop the player\n"
            text = text + ".music addplaylist playlistname url - adds a url to playlistname\n"
            text = text + ".music rmplaylist playlistname url - remove a url from playlistname\n"
            text = text + ".music removeplaylsit playlistname - removes the playlist with playlistname\n"
            text = text + ".music startplaylist playlistname - starts the playlist with the name playlistname\n"
            text = text + ".music skip - skip to next song in playlist\n"
            text = text + ".music getplaylist - shows all playlist for this server\n"
            await client.send_message(message.channel, text)

    else:
        await client.send_message(message.channel, "What do you want?")
        debug.write("red", "What do you want?")