import math

def x(a, b, c):
    d = a + b
    if c == 1:
        return d * 0.18
    if c == 2:
        return d * 0.10
    else:
        print("err")
        return d / 0

print(x(100, 50, 1))
print(x(200, "50", 2))
print(x(10, 20, 3))
