

def is_leap_year(year):
    # leap year
    if (year % 4 == 0) and (year % 100 != 0):
        return True
    elif year % 400 == 0:
        return True
    # not leap year
    elif year % 4 != 0:
        return False
    elif (year % 100 == 0) and (year % 400 != 0):
        return False
