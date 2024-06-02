from telebot.types import Update
from flask import Flask
from flask import request
from flask import Response
from youbot import bot
from handlers import (message_handlers, inline_handlers,
                      callback_handlers, browse_questions,
                      answer_to, browse_anwers, profile,
                      about)

from utils import keyboards  # noqa
from models.engine.storage import init_db

app = Flask(__name__)
init_db()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        update = Update.de_json(request.stream.read().decode('utf-8'))
        bot.process_new_updates([update])
        return Response('ok', status=200)
    else:
        return '<h1>Youbot is Here</h1>'


if __name__ == '__main__':
    app.run()
