import telebot
import random
import os

API_TOKEN = os.environ.get('TELEGRAM_TOKEN', '8662174247:AAEHxJkPdZ6biDaw8WKp1rSLmVsbDfx_hwA')
bot = telebot.TeleBot(API_TOKEN)

GREETINGS = [
    "Happy Father's Day! 🎉 To the world's greatest dad!",
    "Wishing you a wonderful Father's Day filled with love and joy! ❤️",
    "Happy Father's Day to an amazing father! You're the best! 👨‍👧‍👦",
    "Dad, you're my hero! Happy Father's Day! 🦸‍♂️",
    "To the man who has it all - a Happy Father's Day! 🎊",
]

FUNNY_WISHES = [
    "Happy Father's Day! You're not old, you're classic! 😄",
    "Dad, thanks for all the dad jokes! Happy Father's Day! 😂",
    "To the man who thinks he's funny - Happy Father's Day! 🎭",
]

HEARTFELT_WISHES = [
    "Happy Father's Day! Your love and support mean the world to me. 🙏",
    "Dad, thank you for always being there. Happy Father's Day! 💕",
    "Dad, your wisdom and guidance have shaped who I am. Happy Father's Day! 🌳",
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 
        "👋 Welcome to Father's Day Bot! 🎉\n\n"
        "/greeting - Get a greeting\n"
        "/funny - Get a funny message\n"
        "/heartfelt - Get a heartfelt message")

@bot.message_handler(commands=['greeting'])
def send_greeting(message):
    bot.reply_to(message, random.choice(GREETINGS))

@bot.message_handler(commands=['funny'])
def send_funny(message):
    bot.reply_to(message, random.choice(FUNNY_WISHES))

@bot.message_handler(commands=['heartfelt'])
def send_heartfelt(message):
    bot.reply_to(message, random.choice(HEARTFELT_WISHES))

print("🎉 Bot is running!")
bot.infinity_polling()
