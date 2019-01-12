perm = 4

import discord
from commands import debug
from os import path
import shlex
from subprocess import call
from subprocess import run
import time

async def ex(args, message, client, invoke, home_phat):
    if len(args) > 0:
        debug.write("green", args[0])
        if args[0] == "ban":
            memb = message.server.get_member_named(args[1])
            days = args[2]
            client.ban(memb, days)
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description=("%s was baned" % memb)))
            debug.write("green", memb)
        elif args[0] == "kick":
            memb = message.server.get_member_named(args[1])
            client.kick(memb)
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description=("%s was kicked" % memb)))
            debug.write("green", memb)
        elif args[0] == "unban":
            memb = message.server.get_member_named(args[1])
            client.unban(message.server, memb)
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description=("%s was unbaned" % memb)))
            debug.write("green", memb)
        elif args[0] == "nickname":
            memb = message.server.get_member_named(args[1])
            client.change_nickname(memb, args[2])
            debug.write("green", memb + "'s new name is "+ args[2])
        elif args[0] == "role":
            rolename = args[1]
            memb = message.server.get_member_named(args[2])
            role = discord.utils.get(message.server.roles, name=rolename)
            if role == None:
                await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description=("Please enter a valid role %s" % rolename)))
                debug.write("red", "No valide role!")
            else:
                await client.add_roles(memb,role)
                await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description=("role %s was added" % rolename)))
                debug.write("green", "add " + role + " to " + memb)
        elif args[0] == "removerole":
            rolename = args[1]
            memb = message.server.get_member_named(args[2])
            role = discord.utils.get(message.server.roles, name=rolename)
            if role == None:
                await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description=("Please enter a valid role %s" % rolename)))
                debug.write("red", "No valide role!")
            else:
                await client.remove_roles(memb,role)
                await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description=("role %s was removed" % rolename)))
                debug.write("green", "remove " + role + " from " + memb)
        elif args[0] == "shutdown":
            debug.write("red", "Shutdown in 5 sec!")
            time.sleep(5)
            call(['shutdown', '-h', 'now'], shell=False)
        elif args[0] == "reboot":
            debug.write("red", "Reboot in 5 sec!")
            time.sleep(5)
            call(['reboot', '-h', 'now'], shell=False)
        elif args[0] == "exit":
            debug.write("red", "Close bot!")
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description=("close bot!")))
            cmd = shlex.split("pkill -f bot.py")
            run(cmd)
        elif args[0] == "addchatfilter":
            dat = args[1]
            if path.isfile(home_phat + "SETTINGS/" + message.server.id + "/chatFilter.txt"):
                debug.write("green", "chat-filter add " + dat)
                with open(home_phat + "SETTINGS/" + message.server.id + "/chatFilter.txt", "a") as f:
                    f.write(dat+"\n")
                    f.close()
                await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description=("add %s to chatFilter" % dat)))
        elif args[0] == "rmchatfilter":
            dat = args[1]
            if path.isfile(home_phat + "SETTINGS/" + message.server.id + "/chatFilter.txt"):
                debug.write("red", "chat-filter remove " + dat)
                file = open(home_phat + "SETTINGS/" + message.server.id + "/chatFilter.txt","r")
                lines = file.readlines()
                file.close()
                file = open(home_phat + "SETTINGS/" + message.server.id + "/chatFilter.txt","w")
                for line in lines:
                    if line != (dat+"\n"):
                        file.write(line)
                    else:
                        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description=("remove %s from chatFilter" % dat)))
                file.close()
            
    else:
        await client.send_message(message.channel, "What do you want?")        