import telebot
import random
import os
import schedule


token = "7666674896:AAG95S_eVb4T6ytNZac9C_04x786UgvSJOM"
user = 6993321134
folder = 'memes'

bot = telebot.TeleBot(token)

def random_meme():
    files = os.listdir(folder)
    return (os.path.join(folder, random.choice(files))) if files else None

def send_meme():
    meme_path = random_meme()
    if meme_path:
        with open(meme_path, "rb") as meme:
            bot.send_photo(user, meme, caption="Мем дня!")
    else:
        bot.send_message(user, "Немає мемів у папці!")

@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "Привіт! Я буду слати тобі мем кожного ранку!")
    schedule.every().day.at("09:00").do(send_meme)

if __name__ == "__main__":
    bot.polling(none_stop=True)
