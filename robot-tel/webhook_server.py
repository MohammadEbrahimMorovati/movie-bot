# webhook_server.py

from flask import Flask, request
import telebot
import os
from config import BOT_TOKEN
from handlers import start, search, advanced_search, menu

bot = telebot.TeleBot(BOT_TOKEN)

# ثبت همه هندلرها
start.register_handlers(bot)
search.register_handlers(bot)
advanced_search.register_handlers(bot)
menu.register_handlers(bot)

app = Flask(__name__)

# ست کردن webhook فقط یک بار
WEBHOOK_URL = f"https://{os.getenv('RENDER_EXTERNAL_HOSTNAME')}/{BOT_TOKEN}/"
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL)

@app.route(f"/{BOT_TOKEN}/", methods=["POST"])
def receive_update():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return {"ok": True}
