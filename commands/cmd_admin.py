perm = 4

import discord

async def ex(args, message, client, invoke):
    if args[0] == "ban":
        memb = message.server.get_member_named(args[1])
        days = args[2]
        client.ban(memb, days)
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description=("%s was baned" % memb)))
    elif args[0] == "kick":
        memb = message.server.get_member_named(args[1])
        client.kick(memb)
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description=("%s was kicked" % memb)))
    elif args[0] == "unban":
        memb = message.server.get_member_named(args[1])
        client.unban(message.server, memb)
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description=("%s was unbaned" % memb)))
    elif args[0] == "nickname":
        memb = message.server.get_member_named(args[1])
        client.change_nickname(memb, args[2])
    elif args[0] == "role":
        rolename = args[1]
        memb = message.server.get_member_named(args[2])
        role = discord.utils.get(message.server.roles, name=rolename)
        if role == None:
             await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description=("Please enter a valid role %s" % rolename)))
        else:
            await client.add_roles(memb,role)
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description=("role %s was added" % rolename)))
    elif args[0] == "removerole":
        rolename = args[1]
        memb = message.server.get_member_named(args[2])
        role = discord.utils.get(message.server.roles, name=rolename)
        if role == None:
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description=("Please enter a valid role %s" % rolename)))
        else:
            await client.remove_roles(memb,role)
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description=("role %s was removed" % rolename)))
            