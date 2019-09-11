from datetime import datetime, timedelta

def getNowDatetime():
    return datetime.now()

def thirtyDaysLater(dt):
    return (dt + timedelta(days=30)).strftime(r"%Y/%m/%d")
