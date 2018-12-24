import discord
import asyncio as asyncio
from SETTINGS import SECRETS, STATICS
from commands import perms, cmd_bot, cmd_autorole, cmd_help, cmd_clear, cmd_admin, cmd_cat

chat_filter =[] 
client = discord.Client()

file = open("SETTINGS/chatFilter.txt", "r") 
for line in file:
    chat_filter.append(line.rstrip())
file.close()
print("Chat Filter:")
print(chat_filter)

commands ={
    "bot": cmd_bot,
    "autorole": cmd_autorole,
    "help": cmd_help,
    "clear": cmd_clear,
    "admin": cmd_admin,
    "cat": cmd_cat

} 

@client.event
async def on_ready():
    print ("Bot is logged in \n Server(s):")
    for s in client.servers:
        print(" - %s [%s] " % (s.name, s.id))
    await client.change_presence(game=discord.Game(name="with Humans"))

@client.event
async def on_member_join(member):
    await client.send_message(member,"Hey %s!!\n\nWelcome on the %s\n\nNow have a nice day!" % (member.name, member.server.name))
    role = cmd_autorole.get(member.server)
    if not role == None:
        await client.add_roles(member, role)

@client.event
async def on_message(message):
    contens = message.content.lower().split(" ")
    for word in contens:
        if word in chat_filter:
            await client.delete_message(message)

    if message.content.startswith(STATICS.PREFIX):
        invoke = message.content[len(STATICS.PREFIX):].split(" ")[0]
        args = message.content.split(" ")[1:]
        if commands.__contains__(invoke):
            cmd = commands[invoke]
            try:
                if not perms.check(message.author, cmd.perm):
                    await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="You are not allowed to access this command!"))
                    return
                await cmd.ex(args, message, client, invoke)
            except:
                await cmd.ex(args, message, client, invoke)
                pass
        else:
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description=("The command %s is not valid!" % invoke)))

client.run(SECRETS.TOKEN)