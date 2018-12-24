perm = 2

import discord
from commands import debug

async def ex(args, message, client, invoke):
    try:
        amount = int(args[0]) + 1 if len(args) > 0 else 2
    except:
        await client.send_message(channel, embed=discord.Embed(color=discord.Color.red(), description="Please enter a valid value for deleting messages"))
        debug.write("red", "No valid value for clear!")
        return
    
    messages =[]
    async for m in client.logs_from(message.channel, limit=amount):
        messages.append(m)
    
    await client.delete_messages(messages)
