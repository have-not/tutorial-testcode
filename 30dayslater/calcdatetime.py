from datetime import datetime, timedelta

def now_datetime():
    return datetime.now()

def thirty_days_later(dt):
    return (dt + timedelta(days=30)).strftime(r"%Y/%m/%d")
