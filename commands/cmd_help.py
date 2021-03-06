import discord
import asyncio as asyncio
from commands import debug

text = "- \n prefix autorole rolename - set role for new members (.autorole Member)\n "
text = text + "prefix autorole clear - delete the role for new members\n"
text = text + "prefix music help - commands for the music bot\n"
text = text + "prefix clear 5 - delete last 5 messages in channel\n"
text = text + "prefix admin role role_name name - add role to member\n"
text = text + "prefix admin removerole role_name name - remove role from member\n"
text = text + "prefix admin leave - Leave this Server"
text = text + "prefix admin addchatfilter word - add word to chat-filter\n"
text = text + "prefix admin rmchatfilter word - remove word from chat-filter\n"
text = text + "prefix admin kick name - kick a member\n"
text = text + "prefix admin ban name - ban a member\n"
text = text + "prefix admin unban name - unban a member\n"
text = text + "prefix admin name nickname - change nickname from member\n"
text = text + "prefix cat - shows random cat image\n"
text = text + "prefix bot - texting with the bot (\n bot hello\n bot dice - roll the dice\n get-pi 'decimal points - calculate PI example .bot get-pi 100'\n bot oracle Question - answer with yes,no or maybe\n bot bitcoin - get the Exchange rate\n bot write somthing - talk with the bot)\n"
text = text + "default prefix is . example .cat\n"
text = text + "Role System:\n"
text = text + "lvl1 = .bot, .cat, .help .info commands / lvl2 = .music commands / lvl3 = .clear commands / lvl4 = .admin, .autorole commands\n"
text = text + ".admin getpermsrole level (example: .admin getpermsrole lvl2) - show all roles for level 2\n"
text = text + ".admin addpermsrole level rolename (example: .admin addpermsrole lvl2 test) - add role 'test' to level 2\n"
text = text + ".admin rmpermsrole level rolename (example: .admin rmpermsrole lvl2 test) - remove role 'test' from level 2\n"
text = text + ".info - get bot profil"

async def ex(args, message, client, invoke, home_phat):
    await client.send_message(message.channel, text)
    debug.write("yellow", text)

if __name__ == "__main__":
    print("This is a command script, it can not be started directly.")