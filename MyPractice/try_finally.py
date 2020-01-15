# Filename:try_finally.py

import time

try:
    f = open("poem.txt")
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(1)
        print(line),
finally:
    f.close()
    print("Cleaning up...closed the file")


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
