import math

# 1st
degrees = int(input())
rads = round(math.radians(degrees), 6)
print(f"Input degree: {degrees}")
print(f"Output radians: {rads}")

# 2nd
h, b1, b2 = map(int, input().split())
def trapezoidArea(h, b1, b2):
    return (b1+b2)/2 * h
print(trapezoidArea(h, b1, b2))

# 3rd
def polygonArea(n, l):
    apothem = l / 2*math.tan(math.pi/n)
    return (n * l * apothem)/2

n, l = map(int, input().split())
print(round(polygonArea(n, l)))

# 4th
def parallelogramArea(l, h):
    return l*h
l, h = map(int, input().split())
print(parallelogramArea(l, h))