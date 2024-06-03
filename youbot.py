from telebot import TeleBot
import os


def create_bot():
    """
    creates the main bot and reuse it across modules
    """
    token = os.getenv('TOKEN')
    bot = TeleBot(token)
    bot.delete_webhook()
    # bot.set_webhook(url=url)

    return bot


bot = create_bot()
