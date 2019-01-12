import discord
import requests
import json
from commands import debug

async def ex(args, message, client, invoke, home_phat):
    r = requests.get("https://random.cat")
    r = str(r.content)
    r = r.replace("b'","")
    r = r.replace("'","")
    r = r.replace("\\","")
    cach = r.split('id="sidebar">n    <a href="')
    cach = cach[1].split('"><img src')
    url = cach[0]
    debug.write("yellow", url)
    await client.send_message(message.channel, url)