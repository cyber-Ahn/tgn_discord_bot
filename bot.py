home_phat = "/home/pi/tgn_discord_bot/"

from colorama import Fore, Back, Style
import os
os.system('clear')
print (Fore.GREEN + "Load AI")
import discord
import asyncio as asyncio
import shutil
from os import path
from commands import perms, cmd_autorole, cmd_help, cmd_clear, cmd_admin, cmd_cat, debug, cmd_music, cmd_info, cmd_bot
from SETTINGS import SECRETS, STATICS

chat_filter = {}
client = discord.Client()

commands ={
    "bot": cmd_bot,
    "autorole": cmd_autorole,
    "help": cmd_help,
    "clear": cmd_clear,
    "admin": cmd_admin,
    "cat": cmd_cat,
    "music": cmd_music,
    "info": cmd_info

} 

def chatFread(id, home_phat):
    global chat_filter
    file = open(home_phat + "SETTINGS/" + id +"/chatFilter.txt", "r")
    for line in file:
        if id in chat_filter:
            chat_filter[id].append(line.rstrip())
        else:
            chat_filter[id] = [line.rstrip()]
    file.close()

@client.event
async def on_ready():
    print (Fore.GREEN + "Bot is logged in \n Server(s):")
    for s in client.servers:
        print(Fore.RED + " - %s [%s] " % (s.name, s.id))
        if not path.isfile(home_phat + "SETTINGS/" + s.id + "/authorization.json"):
            os.makedirs(home_phat + "SETTINGS/" + s.id)
            shutil.copyfile(home_phat + 'SETTINGS/authorization.json', home_phat + 'SETTINGS/' + s.id + '/authorization.json')
            shutil.copyfile(home_phat + 'SETTINGS/chatFilter.txt', home_phat + 'SETTINGS/' + s.id + '/chatFilter.txt')
        chatFread(s.id, home_phat)
    print(Fore.YELLOW + "Chat Filter:")
    print(chat_filter)
    await client.change_presence(game=discord.Game(name="with humanity"))
    print (Fore.WHITE + "Ready for use")

@client.event
async def on_member_join(member):
    await client.send_message(member,"Hey %s!!\n\nWelcome on the %s\n\nNow have a nice day!" % (member.name, member.server.name))
    role = cmd_autorole.get(member.server, home_phat)
    if not role == None:
        await client.add_roles(member, role)

@client.event
async def on_message(message):
    contens = message.content.lower().split(" ")
    for word in contens:
        if word in chat_filter[message.server.id]:
            await client.delete_message(message)

    if message.content.startswith(STATICS.PREFIX):
        invoke = message.content[len(STATICS.PREFIX):].split(" ")[0]
        args = message.content.split(" ")[1:]
        if commands.__contains__(invoke):
            cmd = commands[invoke]
            debug.write("blue", invoke)
            try:
                if not perms.check(message.author, cmd.perm, message.server.id, home_phat):
                    await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="You are not allowed to access this command!"))
                    debug.write("red", "No access, low level!")
                    return
                await cmd.ex(args, message, client, invoke, home_phat)
            except:
                await cmd.ex(args, message, client, invoke, home_phat)
                pass
            if len(args) > 1:
                if args[0] == "rmchatfilter" or args[0] == "addchatfilter":
                    chat_filter[message.server.id] = []
                    chatFread(message.server.id, home_phat)
                    print(Fore.YELLOW + "Chat Filter:")
                    print(chat_filter)
        else:
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description=("The command %s is not valid!" % invoke)))
            debug.write("red", "No valid command!")

client.run(SECRETS.TOKEN)