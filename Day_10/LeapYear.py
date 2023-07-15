def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Leap year."
            else:
                return "Not leap year."
        else:
            return "Leap year."
    else:
        return "Not leap year."


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    leap_year = is_leap(year)
    month -= 1

    if leap_year == "Leap year." and month_days[1] == month_days[month]:
        return month_days[month] + 1
    else:
        return month_days[month]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)







