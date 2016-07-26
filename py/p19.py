import calendar

first_sundays = 0
for y in range(1901, 2001):
    for m in range(1, 13):
        if calendar.monthcalendar(y, m)[0][6] == 1:
            first_sundays += 1

print first_sundays
