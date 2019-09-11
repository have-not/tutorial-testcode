def getGreetMsg(time=0):
    if 6 < time and time < 10:
        return "good morning!"
    if time < 0 or 23 < time:
        return "time error"
    else:
        return "hello!"
