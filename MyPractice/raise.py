# Filename:raise.py

class ShortInputError(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    s = raw_input("Enter something -->")
    if len(s) < 3:
        raise(ShortInputError(len(s), 3))
except(EOFError):
    print("Why did you do an EOF on me?")
except ShortInputError as e:
    print("ShortInputError: The input was of length %d, \
was expecting at least %d" % (e.length, e.atleast))
else:
    print("No exception was raised.")
