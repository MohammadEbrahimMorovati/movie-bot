# handlers/menu.py
from telebot import types

def register_handlers(bot):
    @bot.message_handler(commands=['menu'])
    def show_menu(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

        markup.add(
            types.KeyboardButton("🔍 جستجو"),
            types.KeyboardButton("⚡ جستجوی پیشرفته"),
            types.KeyboardButton("🎬 تازه‌ها"),
            types.KeyboardButton("🇮🇷 ایرانی"),
            types.KeyboardButton("📺 یوتوب"),
            types.KeyboardButton("💠 دسته‌بندی"),
            types.KeyboardButton("🎬 برترین‌ها")
        )

        bot.send_message(message.chat.id, "📋 منوی اصلی:", reply_markup=markup)
