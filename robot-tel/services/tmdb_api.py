# services/tmdb_api.py

import requests
from config import TMDB_API_KEY

def search_movie(query):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={query}"
    r = requests.get(url)
    data = r.json()

    if data['results']:
        movie = data['results'][0]
        title = movie['title']
        overview = movie.get('overview', 'خلاصه‌ای موجود نیست.')
        return f"🎬 {title}\n\n{overview}"
    else:
        return "❌ فیلمی پیدا نشد."

# -------------------------------
def advanced_search(filters):
    media_type = filters.get("type", "movie")
    base_url = f"https://api.themoviedb.org/3/discover/{media_type}"

    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US",
        "sort_by": "popularity.desc",
        "page": 1
    }

    if "year" in filters:
        params["year" if media_type == "movie" else "first_air_date_year"] = filters["year"]

    if "country" in filters:
        params["region"] = filters["country"]

    if "rating" in filters:
        try:
            rating = float(filters["rating"])
            params["vote_average.gte"] = rating
        except ValueError:
            pass

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        results = data.get("results", [])
    except Exception as e:
        return f"❌ خطا در ارتباط با API:\n{e}"

    if not results:
        return "❌ موردی پیدا نشد."

    output = ""
    for item in results[:5]:
        title = item.get("title") or item.get("name", "بدون عنوان")
        overview = item.get("overview", "خلاصه‌ای موجود نیست.")
        vote = item.get("vote_average", "?")
        output += f"🎬 {title} - 🌟 {vote}\n{overview[:300]}...\n\n"

    return output
