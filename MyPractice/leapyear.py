# Filename:leapyear.py


def isLeapYear(year):
    if year % 100 == 0 and year % 4 == 0:
        return True
    else:
        return False


while(True):
    num = input("Please enter a integer:")
    if num < 0:
        break
    result = isLeapYear(num)
    if result:
        print "is leap year"
    else:
        print "is not leap year"
