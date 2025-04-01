import telebot
import random
import schedule

token = "YOUR TOKEN" # CHANGE THE TEXT "YOUR TOKEN" TO YOUR TELEGRAM BOT TOKEN
user = "user code"   # ADD HERE SOMEONES ID TO ALSO SEND THEM THE MEMES
folder = 'memes'     # YOU NEED TO MAKE A FOLDER IN YOUR PROGRAM CALLED "MEMES" AND THERE YOU CAN ADD YOUR MEMES. THEIR NAME SHOULD BE "1.jpg" and "2.jpg".

bot = telebot.TeleBot(token)

def random_meme():
    files = ["1.jpg", "2.jpg",]  
    if files:
        return f"{folder}/{random.choice(files)}"
    else:
        return None

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
