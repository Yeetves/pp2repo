def myfunc(n):
    return lambda a: a * n

doubleVal = myfunc(2)
tripleVal = myfunc(3)
print(doubleVal(6), tripleVal(7))


nums = [1, 2, 3, 4, 5]
sq = lambda a : a**2
for num in nums:
    print(sq(num), end=" ")
print()

#divide into symbols
n = 987
x = lambda a : a%10
while n!=0:
    print(x(n))
    n //= 10

x = lambda a, b, c: a + b + c
print(x(3, 6, 2))