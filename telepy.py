import telegram
import rss
from telegram import Update
from telegram.ext import Updater, MessageHandler, filters, CommandHandler, CallbackContext

if __name__ == "__main__":
    my_token = '6006682867:AAEHxGvjFanuO_bORsEFNEjSMbIkna_lEyM'
    bot = telegram.Bot(token=my_token)
    updates = bot.getUpdates()
    text = rss.RSScrawler()
    bot.sendMessage(chat_id='5525776231', text=text)
    

