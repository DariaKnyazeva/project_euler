"""
COUNTING SUNDAYS
"""
from calendar import Calendar


if __name__ == "__main__":
    """
    You are given the following information.

    * 1 Jan 1900 was a Monday.
    * Thirty days has September, April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    * A leap year occurs on any year evenly divisible by 4,
    but not on a century unless it is divisible by 400.

    How many Sundays fell on the first of the month during the twentieth century
    (1 Jan 1901 to 31 Dec 2000)?
    """
    print("Problem 19: Counting Sundays")
    # Starting Sunday
    cal = Calendar(firstweekday=6)
    result = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            # Iterating over month days,
            # we are interested in every sunday
            sundays = list(cal.itermonthdays(year, month))[::7]
            result += len([d for d in sundays if d == 1])
    print(result)
