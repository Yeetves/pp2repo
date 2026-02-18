nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x : x%2 == 0, nums))
print(evens)

odds = list(filter(lambda x:x%2 != 0, nums))
print(odds)

nums = [1, 18, 7, 9, 10, 45, 78, 3]
tens = list(filter(lambda x:x//10 != 0, nums))
print(tens)

singles = list(filter(lambda x:x//10 == 0, nums))
print(singles)