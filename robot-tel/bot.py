from config import BOT_TOKEN
import telebot
import os

bot = telebot.TeleBot(BOT_TOKEN)

# ثبت هندلرها مثل قبل
from handlers import start, search, advanced_search, menu
start.register_handlers(bot)
search.register_handlers(bot)
advanced_search.register_handlers(bot)
menu.register_handlers(bot)

# URL و TOKEN
WEBHOOK_URL = f"https://{os.getenv('RENDER_EXTERNAL_HOSTNAME')}/{BOT_TOKEN}/"

# حذف webhook قبلی و ست کردن جدید
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL)
