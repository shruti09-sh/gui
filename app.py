from flask import Flask, render_template, request
from .chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

english_bot = ChatBot("ChatterBot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterBot.corpus.english")
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))

if __name__ == '__main__':
    app.run()
