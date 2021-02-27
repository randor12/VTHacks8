import datetime

start = datetime.date(2021, 2, 27)

today = datetime.date.today()

delta = today - start

def get_diff():
    return delta.days
