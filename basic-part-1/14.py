import datetime

start_date = datetime.date(*(2014, 7, 2))
end_date = datetime.date(*(2014, 7, 11))

diff = abs(end_date - start_date)

print(diff.days)
