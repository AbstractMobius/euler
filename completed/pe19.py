import datetime

a = 0
for i in range(1901,2001):
    for j in range(1,13):
        if datetime.date(i, j, 1).isoweekday() == 7:
            a += 1

print(a)

