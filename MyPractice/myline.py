# Filename:myline.py

def line_conf():
    b = 15
    def line(x):
        return 2 * x + b
    return line

b = 5
myline = line_conf()
print(myline(5))
print(myline.__closure__)
print(myline.__closure__[0].cell_contents)

def line_conf2(a,b):
    def line(x):
        return a * x + b
    return line
line1 = line_conf2(1,1)
line2 = line_conf2(4,5)
print(line1(5),line2(5))
