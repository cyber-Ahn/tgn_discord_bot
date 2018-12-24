import discord
import requests
import json

async def ex(args, message, client, invoke):
    r = requests.get("https://random.cat")
    r = str(r.content)
    r = r.replace("b'","")
    r = r.replace("'","")
    r = r.replace("\\","")
    cach = r.split('id="sidebar">n    <a href="')
    cach = cach[1].split('"><img src')
    url = cach[0] 
    await client.send_message(message.channel, url)