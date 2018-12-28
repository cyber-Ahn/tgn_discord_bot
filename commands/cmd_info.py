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

text2 = ".music join - join your voice channel\n\n"
text2 = text2 + ".music disconnect - disconnect voice channel\n\n"
text2 = text2 + ".music play url - plays the youtube url\n\n"
text2 = text2 + ".music pause - pause the player\n\n"
text2 = text2 + ".music resume - resume to music\n\n"
text2 = text2 + ".music stop - stop the player\n\n"
text2 = text2 + ".music addplaylist playlistname url - adds a url to playlistname\n\n"
text2 = text2 + ".music rmplaylist playlistname url - remove a url from playlistname\n\n"
text2 = text2 + ".music removeplaylsit playlistname - removes the playlist with playlistname\n\n"
text2 = text2 + ".music startplaylist playlistname - starts the playlist with the name playlistname\n\n"
text2 = text2 + ".music skip - skip to next song in playlist\n\n"
text2 = text2 + ".music getplaylist - shows all playlist for this server"

async def ex(args, message, client, invoke):
    embed = discord.Embed(
        title = "RGN Discord Bot Info",
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