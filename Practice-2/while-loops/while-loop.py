i = 1
sum = 0

while i < 10:
    sum += i
    i += 1
print(sum)


j = 0
while j <= 10:
    j += 1
    if j%2 != 0:
        continue
    print(j, end=" ")

print()

k = 0
while k < 50:
    k += 1
    print(k, end = " ")
    if k == 30:
        break