# utils/logger.py

import datetime

def log(message: str, level: str = "INFO"):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] [{level}] {message}")
