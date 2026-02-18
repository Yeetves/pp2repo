import datetime
from zoneinfo import ZoneInfo

print(datetime.datetime.now())

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

# creating date objects
random_date = datetime.datetime(2023, 12, 18)
print(random_date)

# formatting
day = datetime.datetime(2006, 12, 11)
print(day.strftime("%B")) #month full
print(day.strftime("%c")) #local version of date and time
print(day.strftime("%x")) #local version of date
print(day.strftime("%X")) #local version of time

# calculating time differences
myBirthday = datetime.datetime(2006, 12, 11)
this_day = datetime.datetime.now()

diff = this_day - myBirthday
print(diff, diff.total_seconds())

#changing timezones
utc_time = datetime.datetime(2026, 2, 18, tzinfo = ZoneInfo("UTC"))
almaty_time = utc_time.astimezone(ZoneInfo("Asia/Almaty"))

print(utc_time)
print(almaty_time)

