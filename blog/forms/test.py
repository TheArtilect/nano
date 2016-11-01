
def valid_day(day):
    if (day.isdigit()):
        return day
    else:
        return None


valid_day('0')
# => None
valid_day('1')
# => 1
valid_day('15')
# => 15
valid_day('500')
# => None
