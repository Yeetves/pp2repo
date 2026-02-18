# 1st
n = int(input())
squares = (pow(x, 2) for x in range (1, n+1))
print(list(squares))

# 2nd
def generate_evens(n):
    for i in range(n+1):
        if i%2 == 0:
            yield i

n = int(input())
res = list(map(str, generate_evens(n)))
for r in res:
    print(r, end = " ")
print()

# 3rd
def isDivisible(n):
    for i in range(n+1):
        if i%3 == 0 and i%4 == 0:
            yield i
n = int(input())
result = list(map(str, isDivisible(n)))
for res in result:
    print(res, end = " ")
print()

# 4th
a, b = map(int, input().split())
squares = (pow(x, 2) for x in range(a, b+1))
for square in list(squares):
    print(square, end=" ")
print()

def nums_down(n):
    for i in range(n, -1, -1):
        yield i
n = int(input())
results = list(map(str, nums_down(n)))
for result in results:
    print(result, end = " ")
