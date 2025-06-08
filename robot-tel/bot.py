# bot.py
import telebot
from config import BOT_TOKEN
from handlers import start, search, menu , advanced_search

bot = telebot.TeleBot(BOT_TOKEN)

# ثبت هندلرها

start.register_handlers(bot)
menu.register_handlers(bot)
search.register_handlers(bot)
advanced_search.register_handlers(bot)

print("🤖 ربات در حال اجراست...")
bot.infinity_polling()
