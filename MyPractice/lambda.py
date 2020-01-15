# Filename:lambda.py

def make_repeater(n):
    return lambda s : s * n

twice = make_repeater(2)
print(twice("ha"))
print(twice(5))

# print(eval(2 * 3))

exec("print('hello world')")

i = []
print("tuple:", repr(i))
i.append("item")
print("tuple:", repr(i))

j = {}
print("dict:", repr(j))
j["key1"] = "value1"
print("dict:", repr(j))
