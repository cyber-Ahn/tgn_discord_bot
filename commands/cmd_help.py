import discord
import asyncio as asyncio
from commands import debug

text = "- \n prefix autorole rolename - set role for new members (.autorole Member)\n "
text = text + "prefix autorole clear - delete the role for new members\n"
text = text + "prefix music help - commands for the music bot\n"
text = text + "prefix clear 5 - delete last 5 messages in channel\n"
text = text + "prefix admin role role_name name - add role to member\n"
text = text + "prefix admin removerole role_name name - remove role from member\n"
text = text + "prefix admin kick name - kick a member\n"
text = text + "prefix admin ban name - ban a member\n"
text = text + "prefix admin unban name - unban a member\n"
text = text + "prefix admin name nickname - change nickname from member\n"
text = text + "prefix cat - shows random cat image\n"
text = text + "prefix bot - texting with the bot (\n bot hello\n bot dice - roll the dice\n bot oracle Question - answer with yes,no or maybe\n bot bitcoin - get the Exchange rate\n *bot write somthing - talk with the bot)\n"
text = text + "default prefix is . example .cat"

async def ex(args, message, client, invoke):
    await client.send_message(message.channel, text)
    debug.write("yellow", text)
