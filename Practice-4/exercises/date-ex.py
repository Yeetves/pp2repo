import datetime

# 1st
current_date = datetime.datetime.now()
print(current_date - datetime.timedelta(days = 5))

# 2nd
for i in range(-1, 2):
    print(current_date + (i) * datetime.timedelta(days=1))

# 3rd
print(current_date.replace(microsecond=0))

# 4th
two_days = datetime.timedelta(days = 2)
print(two_days.total_seconds())