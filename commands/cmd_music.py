perm = 2

from commands import debug
from SETTINGS import SECRETS
from os import path
from urllib.parse import urlparse
from urllib import request
import urllib
import discord
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time
import youtube_dl

players = {}
queues = {}

sp_id = SECRETS.spotify_id
sp_secret = SECRETS.spotify_secret
debug.write("blue", "Spotify ID:" + sp_id + "\nSpotify Secret:" + sp_secret)

global queues
global players

def get_sp_top_tracks(name, max):
    re_out = {}
    num = 1
    client_credentials_manager = SpotifyClientCredentials(sp_id, sp_secret)
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    results = spotify.search(q='artist:' + name, type='artist')
    uri = results['artists']['items'][0]['uri']
    debug.write("green", uri)
    results = spotify.artist_top_tracks(uri)
    for track in results['tracks'][:max]:
        name_s = 'name;'+track['name']
        debug.write("green", track['name'])
        prev = 'preview;'+track['preview_url']
        uri = 'uri;'+track['uri']
        url = 'url;https://open.spotify.com/track/{}'.format(track['uri'].split(":")[2])
        re_out[num]=[name_s]
        re_out[num].append(prev)
        re_out[num].append(uri)
        re_out[num].append(url)
        num = num + 1
    return re_out

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
    elif "soundcloud.com" in url:
        return True
    else:
        return False

def saveFile(message, name, url, home_phat):
    if not path.isdir(home_phat + "playlist/" + message.server.id):
        os.makedirs(home_phat + "playlist/" + message.server.id)
    with open(home_phat + "playlist/" + message.server.id + "/" + name, "a") as f:
        f.write(url+"\n")
        f.close()

def check_in_list(message, name, url, home_phat):
    if not path.isdir(home_phat + "playlist/" + message.server.id):
        return "no"
    elif not path.isfile(home_phat + "playlist/" + message.server.id + "/" + name):
        return "no"
    else:
        file = open(home_phat + "playlist/" + message.server.id + "/" + name,"r")
        lines = file.readlines()
        file.close()
        if (url+"\n") in lines:
            return "yes"
        else:
            return "no"

def removeFile(message, name, home_phat):
    if path.isfile(home_phat + "playlist/" + message.server.id + "/" + name):
        os.remove(home_phat + "playlist/" + message.server.id + "/" + name)

def removeUrl(message, name, url, home_phat):
    if path.isfile(home_phat + "playlist/" + message.server.id + "/" + name):
        file = open(home_phat + "playlist/" + message.server.id + "/" + name,"r")
        lines = file.readlines()
        file.close()
        file = open(home_phat + "playlist/" + message.server.id + "/" + name,"w")
        for line in lines:
            if line != (url+"\n"):
                file.write(line)
        file.close()

def check_queue(id, home_phat):
    if queues[id] != []:
        player = queues[id].pop(0)
        players[id] = player 
        player.start()
        rv = read_volume(id, home_phat)
        players[id].volume = rv
    else:
        queues.pop(id)

def save_volume(message, vol, home_phat):
    if not path.isdir(home_phat + "SETTINGS/" + message.server.id):
        os.makedirs(home_phat + "SETTINGS/" + message.server.id)
    with open(home_phat + "SETTINGS/" + message.server.id + "/volume", "w") as f:
        f.write(str(vol))
        f.close()

def read_volume(id, home_phat):
    vol = 1.0
    if path.isfile(home_phat + "SETTINGS/" + id + "/volume"):
        file = open(home_phat + "SETTINGS/" + id + "/volume","r")
        lines = file.readlines()
        file.close()
        for x in lines:
            vol = float(x)
        return vol
    else:
         return vol

async def ex(args, message, client, invoke, home_phat):
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
        
        elif args[0] == "pause":
            debug.write("green", "pause")
            id = message.server.id
            players[id].pause()
            await client.send_message(message.channel, "player paused")
        
        elif args[0] == "stop":
            debug.write("red", "stop")
            queues.pop(message.server.id)
            id = message.server.id
            players[id].stop()
            await client.send_message(message.channel, "player stoped")
        
        elif args[0] == "resume":
            debug.write("green", "resume")
            id = message.server.id
            players[id].resume()
            await client.send_message(message.channel, "resume player")

        elif args[0] == "volume":
            vol = int(args[1])
            id = message.server.id
            vol = vol / 100
            debug.write("green","set volume to: "+str(vol))
            await client.send_message(message.channel, "set volume to: " + str(vol))
            players[id].volume = vol
            save_volume(message, vol, home_phat)
         
        elif args[0] == "addplaylist":
            name = args[1]
            url = args[2]
            if url_check(url) and youtube_check(url):
                if check_in_list(message, name, url, home_phat) == "no":
                    saveFile(message, name, url, home_phat)
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
            removeUrl(message, name, url, home_phat)
            debug.write("red", "remove " + url + " from playlist: " + name)
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description=("remove %s from playlist: %s" % (url, name))))
        
        elif args[0] == "removeplaylist":
            name = args[1]
            removeFile(message, name, home_phat)
            debug.write("red", "remove playlist: " + name)
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description=("remove playlist: %s" % name)))
        
        elif args[0] == "startplaylist":
            name = args[1]
            debug.write("green", "Load playlist")
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description=("Loade Playlist: %s please wait!" % name)))
            server = message.server
            id = server.id
            if id in players:
                players[id].stop()
            voice_client = client.voice_client_in(server)
            if path.isfile(home_phat + "playlist/" + message.server.id + "/" + name):
                file = open(home_phat + "playlist/" + message.server.id + "/" + name,"r")
                lines = file.readlines()
                file.close()
            for line in lines:
                url = line.rstrip()
                time.sleep(5)
                try:
                    player = await voice_client.create_ytdl_player(url, after= lambda: check_queue(server.id, home_phat))
                    if server.id in queues:
                        queues[server.id].append(player)
                    else:
                        queues[server.id] = [player]
                except:
                    await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Somthing is wrong!"))
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description=("Loaded Playlist: %s" % name)))
            player = queues[id].pop(0)
            players[server.id] = player
            player.start()
            rv = read_volume(id, home_phat)
            players[id].volume = rv

        elif args[0] == "play":
            url = args[1]
            server = message.server
            id = server.id
            pla = "no"
            if not id in queues:
                pla = "yes"
            debug.write("green", "add song")
            url = args[1]
            voice_client = client.voice_client_in(server)
            if url_check(url) and youtube_check(url):
                try:
                    await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description=("Load and add Song: %s" % url)))
                    player = await voice_client.create_ytdl_player(url, after= lambda: check_queue(server.id, home_phat))
                    if server.id in queues:
                        queues[server.id].append(player)
                    else:
                        queues[server.id] = [player]
                except:
                    await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Somthing is wrong!"))
            else:
                url = youtube_search(args)
                try:
                    await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description=("Load and add Song: %s" % url)))
                    player = await voice_client.create_ytdl_player(url, after= lambda: check_queue(server.id, home_phat))
                    if server.id in queues:
                        queues[server.id].append(player)
                    else:
                        queues[server.id] = [player]
                except:
                    await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Somthing is wrong!"))
            if pla == "yes":
                player = queues[id].pop(0)
                players[server.id] = player
                player.start()
                rv = read_volume(id, home_phat)
                players[id].volume = rv

        elif args[0] == "skip":
            debug.write("red", "skip")
            id = message.server.id
            players[id].stop()
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description="skip song!"))
        
        elif args[0] == "getplaylist":
            debug.write("green", "print all Playlists")
            file_l = ""
            for files in os.listdir(home_phat + "playlist/" + message.server.id):
                file_l = file_l + files + "\n"
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description=file_l))
            debug.write("yellow", file_l)
        
        elif args[0] == "splay":
            #.music splay 2 Led Zeppelin
            name = args.__str__()[15:-1].replace(",", "").replace("'", "")
            num_song = int(args[1])
            debug.write("green", name)
            debug.write("green", str(num_song))
            sp_data = get_sp_top_tracks(name,10)[num_song]
            print(sp_data) 


        elif args[0] == "help":
            text = ".music join - join your voice channel\n"
            text = text + ".music disconnect - disconnect voice channel\n"
            text = text + ".music play url/name - plays the youtube/soundcloud-url or song from name(only youtube)\n"
            text = text + ".music pause - pause the player\n"
            text = text + ".music resume - resume to music\n"
            text = text + ".music stop - stop the player\n"
            text = text + ".music volume 50 - set volume to 50% (steps: 0, 10, 20 ... , 200)\n"
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

if __name__ == "__main__":
    print("This is a command script, it can not be started directly.")