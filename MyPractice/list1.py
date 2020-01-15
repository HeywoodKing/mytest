# Filename:list1.py

listone = [2, 3, 4]
listtwo = [2 * i for i in listone if i > 2]
print(listtwo)

def powersum(power, *args):
    '''Return the sum of each argument raised to specified power.'''
    total = 0
    for i in args:
        total += pow(i, power)
    return total

val = powersum(2, 2, 2, 2, 2)

print(val)

