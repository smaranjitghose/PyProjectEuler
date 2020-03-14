from itertools import repeat
from datetime import timedelta, date


def day_gen():
    days = 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split()
    while True:
        yield from iter(days)


def date_gen(d=1, m=1, y=1900):
    while True:
        if m in {4, 6, 9, 11}:
            yield from zip(range(d, 30 + 1), repeat(m), repeat(y))
        elif m is 2:
            if leap_year(y):
                yield from zip(range(d, 29 + 1), repeat(m), repeat(y))
            else:
                yield from zip(range(d, 28 + 1), repeat(m), repeat(y))
        else:
            yield from zip(range(d, 31 + 1), repeat(m), repeat(y))

        if m is 12:
            y += 1
        else:
            m += 1


def day_date_gen(stop=(31, 12, 2000)):
    g = zip(day_gen(), date_gen())
    while True:
        next_day = next(g)
        yield next_day
        if next_day[1] == stop:
            break


def leap_year(y):
    if y % 4 is 0:
        if y % 100 is not 0:
            return True
        else:
            if y % 400 is 0:
                return True
    return False

def daterange(start, end):
    for n in range(int((end - start).days)):
        yield start + timedelta(n)


if __name__ == '__main__':
#    g = day_date_gen()
#    while True:
#        day, date = next(g)
#        print(day, date)
#        if date == (31, 12, 1900):
#            break
#    ans = sum(
#            day is 'Sunday' and date[0] is 1
#            for day, date
#            in g
#    )

    start = date(1901, 1, 1)
    end = date(2000, 12, 31)
    ans = sum(
            date.weekday() == 6 and date.day == 1
            for date in daterange(start, end)
    )
    print(ans)
