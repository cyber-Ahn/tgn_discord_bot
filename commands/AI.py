from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot("TGN_Bot")
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train("chatterbot.corpus.english")

def ask_ai(msg):
    try:
        replay = bot.get_response(msg)
        return replay
    except:
        return "Somthing is wrong! Try again."
