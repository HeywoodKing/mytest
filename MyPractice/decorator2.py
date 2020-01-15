# Filename:decorator2.py

def decorator(F):
    def new_F(a, b):
        print("input:", a, b)
        return F(a, b)
    return new_F

@decorator
def square_sum(a, b):
    return a**2 + b**2

@decorator
def square_diff(a, b):
    return a**2 - b**2

print(square_sum(3, 4))
print(square_diff(3, 4))


def pre_str(pre=''):
    def decorator(F):
        def new_F(a, b):
            print(pre + "input", a, b)
            return F(a, b)
        return new_F
    return decorator

@pre_str('^_^')
def square_sum2(a, b):
    return a**2 + b**2

@pre_str('T_T')
def square_diff2(a, b):
    return a**2 - b**2

print(square_sum2(3,4))
print(square_diff2(3,4))
