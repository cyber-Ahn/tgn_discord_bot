perm = 4

import discord
import os
import shutil
from os import path
from commands import debug

async def error(content, channel, client):
    await client.send_message(channel, embed=discord.Embed(color=discord.Color.red(), description=content))

def get(server, home_phat):
    f = home_phat + "SETTINGS/" + server.id + "/autorole"
    if path.isfile(f):
        with open(f) as f:
            return discord.utils.get(server.roles, id=f.read())
    else:
        return None

def saveFile(id, server, home_phat):
    if not path.isdir(home_phat + "SETTINGS/" + server.id):
        os.makedirs(home_phat + "SETTINGS/" + server.id)
    with open(home_phat + "SETTINGS/" + server.id + "/autorole", "w") as f:
        f.write(id)
        f.close()


async def ex(args, message, client, invoke, home_phat):
    if len(args) > 0:
        rolename = args.__str__()[1:-1].replace(",", "").replace("'", "")
        if rolename == "clear":
            os.remove(home_phat + "SETTINGS/" + message.server.id + "/autorole")
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description="Successfuly delete autorole" ))
            debug.write("red", "Autorole deleted!")
        else:
            role = discord.utils.get(message.server.roles, name=rolename)
            if role == None:
                await error("Please enter a valid role", message.channel, client)
                debug.write("red", "No valide role!")
            else:
                try:
                    saveFile(role.id, message.server, home_phat)
                    debug.write("green", "Autorole set")
                    await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description="Successfuly set autorole to role '%s'" % role.name))
                except Exception:
                    await error("Something went wrong while saving autorole", message.channel, client)
                    debug.write("red", "Somthing is wrong!")
                    raise Exception