from calendar import TextCalendar

year = 0
month = 1

while True:
    year = abs(int(input('Enter the year: ')))

    if year:
        break

while True:
    month = abs(int(input('Enter the month: ')))
    
    if month <= 12 and month > 0:
        break
    else:
        print('The number must be in range of 1 to 12')

calendar = TextCalendar(firstweekday=0)

calendar.prmonth(year, month)
