import datetime as dt

now = dt.datetime.now()  # 2021-05-26 05:44:28.906128
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
day_of_week = now.weekday()  # weekday começa com 0 para segunda-feira
print(year, month, day, hour, minute, second, day_of_week)

date_of_birth = dt.datetime(year=1983, month=2, day=9, hour=10, minute=44)
print(type(date_of_birth))
print(date_of_birth)
