perm = 4

import discord
import os
import shutil
from os import path

async def error(content, channel, client):
    await client.send_message(channel, embed=discord.Embed(color=discord.Color.red(), description=content))

def get(server):
    f = "SETTINGS/" + server.id + "/autorole"
    if path.isfile(f):
        with open(f) as f:
            return discord.utils.get(server.roles, id=f.read())
    else:
        return None

def saveFile(id, server):
    if not path.isdir("SETTINGS/" + server.id):
        os.makedirs("SETTINGS/" + server.id)
    with open("SETTINGS/" + server.id + "/autorole", "w") as f:
        f.write(id)
        f.close()


async def ex(args, message, client, invoke):
    if len(args) > 0:
        rolename = args.__str__()[1:-1].replace(",", "").replace("'", "")
        if rolename == "clear":
            shutil.rmtree("SETTINGS/"+message.server.id)
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description="Successfuly delete autorole" ))
        else:
            role = discord.utils.get(message.server.roles, name=rolename)
            if role == None:
                await error("Please enter a valid role", message.channel, client)
            else:
                try:
                    saveFile(role.id, message.server)
                    await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description="Successfuly set autorole to role '%s'" % role.name))
                except Exception:
                    await error("Something went wrong while saving autorole", message.channel, client)
                    raise Exception