from telebot import TeleBot


def create_bot():
    """
    creates the main bot and reuse it across modules
    """
    token = '7115257571:AAG2Gr-n3Npl87FAKKgNyEniviyTu-__AMA'
    url = 'https://faithful-wealthy-bullfrog.ngrok-free.app/'
    bot = TeleBot(token)
    bot.delete_webhook()
    bot.set_webhook(url=url)

    return bot


bot = create_bot()
