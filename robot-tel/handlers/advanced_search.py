# handlers/advanced_search.py

from telebot import types
from services.tmdb_api import advanced_search

# دیکشنری برای ذخیره فیلترهای هر کاربر
user_filters = {}

def register_handlers(bot):

    @bot.message_handler(func=lambda msg: msg.text == "⚡ جستجوی پیشرفته")
    def advanced_search_menu(message):
        markup = types.InlineKeyboardMarkup(row_width=2)

        markup.add(
            types.InlineKeyboardButton("🎬 فیلم ✅", callback_data="type_movie"),
            types.InlineKeyboardButton("📺 سریال", callback_data="type_series"),
            types.InlineKeyboardButton("🌍 کشور", callback_data="filter_country"),
            types.InlineKeyboardButton("💣 سال تولید", callback_data="filter_year"),
            types.InlineKeyboardButton("🌟 امتیاز", callback_data="filter_rating"),
            types.InlineKeyboardButton("⭐ ژانر", callback_data="filter_genre"),
            types.InlineKeyboardButton("🗣️ دوبله / زیرنویس", callback_data="filter_lang"),
            types.InlineKeyboardButton("✅ جستجو", callback_data="do_search"),
            types.InlineKeyboardButton("♻️ ریست", callback_data="reset_filters")
        )

        bot.send_message(message.chat.id, "⚙️ فیلترهای فعال جستجو:", reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: True)
    def handle_filter(call):
        user_id = call.from_user.id

        if user_id not in user_filters:
            user_filters[user_id] = {}

        if call.data == "type_movie":
            user_filters[user_id]["type"] = "movie"
            bot.answer_callback_query(call.id, "🎬 نوع: فیلم انتخاب شد.")

        elif call.data == "type_series":
            user_filters[user_id]["type"] = "tv"
            bot.answer_callback_query(call.id, "📺 نوع: سریال انتخاب شد.")

        elif call.data == "filter_country":
            bot.send_message(call.message.chat.id, "🌍 لطفاً نام کشور را وارد کن:")
            bot.register_next_step_handler(call.message, lambda m: set_filter(user_id, "country", m.text))

        elif call.data == "filter_year":
            bot.send_message(call.message.chat.id, "💣 لطفاً سال تولید را وارد کن (مثلاً 2022):")
            bot.register_next_step_handler(call.message, lambda m: set_filter(user_id, "year", m.text))

        elif call.data == "filter_rating":
            bot.send_message(call.message.chat.id, "🌟 لطفاً حداقل امتیاز را وارد کن (مثلاً 7.5):")
            bot.register_next_step_handler(call.message, lambda m: set_filter(user_id, "rating", m.text))

        elif call.data == "reset_filters":
            user_filters[user_id] = {}
            bot.answer_callback_query(call.id, "♻️ فیلترها ریست شدند.")

        elif call.data == "do_search":
            run_search(call.message, user_filters.get(user_id, {}))

def set_filter(user_id, key, value):
    if user_id not in user_filters:
        user_filters[user_id] = {}
    user_filters[user_id][key] = value

def run_search(message, filters):
    result = advanced_search(filters)
    message.bot.send_message(message.chat.id, result)
