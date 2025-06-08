# handlers/menu.py

from telebot import types

def register_handlers(bot):
    @bot.message_handler(commands=['start', 'menu'])  # هر دو دستور فعال
    def show_menu(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        markup.add(
            types.KeyboardButton("جستجو پیشرفته ⚡"), types.KeyboardButton("جستجو 🔍"),
            types.KeyboardButton("یوتوب 🔴"), types.KeyboardButton("ایرانی 🇮🇷"),
            types.KeyboardButton("زیرنویس 🔍"), types.KeyboardButton("تازه‌ها 🔥"),
            types.KeyboardButton("پروفایل من 🧑🏻‍💼"), types.KeyboardButton("پلن‌ها 🎭"),
            types.KeyboardButton("سینما نیوز 🗞️"), types.KeyboardButton("تاریخچه 🧾"),
            types.KeyboardButton("جدول پخش 🗓️"), types.KeyboardButton("دسته‌بندی 💠"),
            types.KeyboardButton("برترین‌ها 🎬"), types.KeyboardButton("پرترین‌ها 📩"),
            types.KeyboardButton("پیشنهاد‌ی 🎲"), types.KeyboardButton("بیشتر ➕")
        )

        bot.send_message(message.chat.id, "📋 منوی اصلی ربات:", reply_markup=markup)
