# handlers/search.py
from services.tmdb_api import search_movie

def register_handlers(bot):
    @bot.message_handler(func=lambda msg: True)
    def search_handler(message):
        result = search_movie(message.text)
        bot.send_message(message.chat.id, result)
