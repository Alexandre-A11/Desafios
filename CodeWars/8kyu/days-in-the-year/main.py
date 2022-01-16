def year_days(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                days = 366
            else:
                days = 365
        else:
            days = 366
    else:
        days = 365

    return f"{year} has {days} days"


print(year_days(2100))
