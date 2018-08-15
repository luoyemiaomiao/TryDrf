import datetime
def dayofyear():
    year = input('年:')
    month = input('月:')
    day = input('天:')
    date1 = datetime.date(year=int(year),month=int(month),day=int(day))
    date2 = datetime.date(year=int(year),month=1,day=1)
    return (date1-date2 + 1 ).days
day1 = dayofyear()

