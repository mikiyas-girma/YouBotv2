from telebot.types import Update
from flask import Flask
from flask import request
from flask import Response
from youbot import bot

# ngrok http --domain=faithful-wealthy-bullfrog.ngrok-free.app 5000


app = Flask(__name__)


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'welcome to the youbot')


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        update = Update.de_json(request.stream.read().decode('utf-8'))
        bot.process_new_updates([update])
        return Response('ok', status=200)
    else:
        return '<h1>Youbot is Here</h1>'


# https://api.telegram.org/bot7115257571:AAG2Gr-n3Npl87FAKKgNyEniviyTu-__AMA/getMe
# https://api.telegram.org/bot7115257571:AAG2Gr-n3Npl87FAKKgNyEniviyTu-__AMA/sendMessage?chat_id=796663862&text='Hello User'
# https://api.telegram.org/bot7115257571:AAG2Gr-n3Npl87FAKKgNyEniviyTu-__AMA/setWebhook?url=https://1d375f472ca423f50fc73dcf68a62bce.serveo.net/


if __name__ == '__main__':
    app.run()
