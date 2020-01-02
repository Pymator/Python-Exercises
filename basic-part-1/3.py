import datetime

current_date = datetime.date.today()
current_time = datetime.datetime.now().strftime("%H:%M:%S")

print('Current date and time:')
print(current_date, current_time)
