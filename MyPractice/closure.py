# Filename:closure.py

# reusability

def line_conf():
    def line(x):
        return 2 * x + 1
    print(line(5))


line_conf()
#这里就不能调用了，调用会出错
# print(line(5))

