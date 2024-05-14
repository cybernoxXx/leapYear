def isLeapYear(year):
    # Check if year is not divisible by 4
    if year % 4 != 0:
        return False
    # Check if year is not divisible by 100, if is not divisible by 4 and 100 is a leap year
    elif year % 100 != 0:
        return True
    # Check if year is not divisible by 400, is in not divisible by 4 and 400 but it's divisible by 100 is a leap year
    elif year % 400 != 0:
        return False
    # Return true in all the other cases
    return True

assert isLeapYear(1999) == False
assert isLeapYear(2000) == True
assert isLeapYear(2001) == False
assert isLeapYear(2004) == True
assert isLeapYear(2100) == False
assert isLeapYear(2400) == True
