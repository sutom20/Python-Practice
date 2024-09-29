user_input = int(input('Please enter the year you want to check\n'))

def is_leap_year(year):
    """this function takes year as user's input and returns a boolean whether given year is leap year or not"""
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False


print(is_leap_year(user_input))

