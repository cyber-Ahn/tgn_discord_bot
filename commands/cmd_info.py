import discord
text = "prefix autorole rolename - set role for new members (.autorole Member)\n\n"
text = text + "prefix autorole clear - delete the role for new members\n\n"
text = text + "prefix music help - commands for the music bot\n\n"
text = text + "prefix clear 5 - delete last 5 messages in channel\nv"
text = text + "prefix admin role role_name name - add role to member\n\n"
text = text + "prefix admin removerole role_name name - remove role from member\n\n"
text = text + "prefix admin kick name - kick a member\n\n"
text = text + "prefix admin ban name - ban a member\n\n"
text = text + "prefix admin unban name - unban a member\n\n"
text = text + "prefix admin name nickname - change nickname from member\n\n"
text = text + "prefix cat - shows random cat image\n\n"
text = text + "prefix bot - texting with the bot (\n bot hello\n bot dice - roll the dice\n bot oracle Question - answer with yes,no or maybe\n bot bitcoin - get the Exchange rate\n *bot write somthing - talk with the bot)\n\n"
text = text + "default prefix is . example .cat"
text = text + "Role System:\n"
text = text + "lvl1 = .bot, .cat, .help .info commands / lvl2 = .music commands / lvl3 = .clear commands / lvl4 = .admin, .autorole commands\n"
text = text + ".admin getpermsrole level (example: .admin getpermsrole lvl2) - show all roles for level 2\n"
text = text + ".admin addpermsrole level rolename (example: .admin addpermsrole lvl2 test) - add role 'test' to level 2\n"
text = text + ".admin rmpermsrole level rolename (example: .admin rmpermsrole lvl2 test) - remove role 'test' from level 2\n"

text2 = ".music join - join your voice channel\n\n"
text2 = text2 + ".music disconnect - disconnect voice channel\n\n"
text2 = text2 + ".music play url/name - plays the youtube/soundcloud-url or song from name(only youtube)\n\n"
text2 = text2 + ".music pause - pause the player\n\n"
text2 = text2 + ".music resume - resume to music\n\n"
text2 = text2 + ".music stop - stop the player\n\n"
text2 = text2 + ".music addplaylist playlistname url - adds a url to playlistname\n\n"
text2 = text2 + ".music rmplaylist playlistname url - remove a url from playlistname\n\n"
text2 = text2 + ".music removeplaylsit playlistname - removes the playlist with playlistname\n\n"
text2 = text2 + ".music startplaylist playlistname - starts the playlist with the name playlistname\n\n"
text2 = text2 + ".music skip - skip to next song in playlist\n\n"
text2 = text2 + ".music getplaylist - shows all playlist for this server"

async def ex(args, message, client, invoke, home_phat):
    embed = discord.Embed(
        title = "TGN Discord Bot Info",
        description = "This is a bot with chat filter, chat AI and music-bot with playlist for each user in the Server",
        colour = discord.Colour.blue()
    )
    embed.set_footer(text="created by cyber Ahn")
    embed.set_image(url='http://caworks-sl.de/data/download/bot.jpg')
    embed.set_thumbnail(url='http://caworks-sl.de/data/download/bot.jpg')
    embed.set_author(name='TGN_Bot', icon_url='http://caworks-sl.de/data/download/bot.jpg')
    embed.add_field(name='Commands:', value=text, inline=False)
    embed.add_field(name='Music Commands:', value=text2, inline=False)
    await client.send_message(message.channel, embed=embed)

if __name__ == "__main__":
    print("This is a command script, it can not be started directly.")