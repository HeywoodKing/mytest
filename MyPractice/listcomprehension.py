# Filename:listcomprehension.py
#±íÍÆµ¼
L = []
for x in range(10):
    L.append(x**2)
    print L

x1 = [1,3,5]
y1 = [9,12,13]
LP = [x**2 for (x,y) in zip(x1,y1) if y > 10]
print LP
