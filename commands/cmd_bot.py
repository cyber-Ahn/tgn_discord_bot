perm = 1

from commands import AI, debug
import aiohttp
import discord
import json
import random
import time

async def ex(args, message, client, invoke):
    if len(args) > 0:
        if "hello" in args:
            debug.write("blue", args[0])
            name = str(message.author)
            cach = name.split("#")
            name = cach[0]
            await client.send_message(message.channel, ("Hello %s" % name))
            debug.write("yellow", "Hello " + name)
        elif "dice" in args:
            debug.write("blue", args[0])
            num = str(random.randint(1,6))
            await client.send_message(message.channel, "Rolling Dice")
            time.sleep(2)
            await client.send_message(message.channel, ("Your Number is %s" % num))
            debug.write("yellow", "Your number is" + num)
        elif "oracle" in args:
            debug.write("blue", args[0])
            num = random.randint(0,2)
            answers = ["yes", "no", "maybe"]
            await client.send_message(message.channel, "I thinking....")
            time.sleep(1.5)
            await client.send_message(message.channel, ("%s" % answers[num]))
            debug.write("yellow", answers[num])
        elif "cookie" in args:
            debug.write("blue", args[0])
            num = random.randint(0,2)
            answers = ["yes", "no", "maybe"]
            await client.send_message(message.channel, ":cookie:")
            debug.write("yellow", ":cookie:")
        elif "bitcoin" in args:
            debug.write("blue", args[0])
            url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
            async with aiohttp.ClientSession() as session:
                raw_response = await session.get(url)
                response = await raw_response.text()
                response = json.loads(response)
                await client.send_message(message.channel, ("Bitcoin price is: $" + response['bpi']['USD']['rate']))
        else:
            msg = args.__str__()[1:-1].replace(",", "").replace("'", "")
            debug.write("blue", msg)
            answ = AI.ask_ai(msg)
            await client.send_message(message.channel, answ)
    else:
        await client.send_message(message.channel, "What do you want?")