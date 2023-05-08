import telegram
from dart_rss import RSS
from time import sleep

class dart:

    def __init__(self):
        my_token = '6006682867:AAEHxGvjFanuO_bORsEFNEjSMbIkna_lEyM'
        self.last_message = ""
        self.interval = 2
        self.dart = RSS()
        self.bot = telegram.Bot(token=my_token)

    def chat_all(self, bot, updates,message):
        id = [k.message.chat_id for k in updates]
        for i in id:
            bot.sendMessage(chat_id=i, text=message)

    def dart_message(self):
        
        updates = self.bot.getUpdates()
        #print(updates[1].message.chat_id)
        
        text = self.dart.get_data()
        print(text)
        if text == None:
            pass
        else:
            for i in text:
                #bot.sendMessage(chat_id='5525776231', text=i)
                self.chat_all(self.bot, updates, i)
                self.last_message = dart.last

    def wait(self):
        while True:
            self.dart_message()
            sleep(120)
        