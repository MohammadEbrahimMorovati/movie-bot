# utils/helper.py

def truncate_text(text, max_length=4000):
    """اگر متن طولانی بود، اون رو کوتاه می‌کنه برای ارسال در تلگرام"""
    return text if len(text) <= max_length else text[:max_length] + "..."
