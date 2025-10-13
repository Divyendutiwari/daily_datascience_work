from datetime import date
mow=date.today()
print(mow)
yesterday=mow.replace(day=mow.day-1)
print(yesterday)