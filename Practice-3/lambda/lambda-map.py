nums = [1, 2, 3, 4, 5]
squares = list(map(lambda a : a**2, nums))
print(squares)

moved_nums = list(map(lambda a : a+10, nums))
print(moved_nums)

scaled_nums = list(map(lambda a : a*10, nums))
print(scaled_nums)

fourth_pow = list(map(lambda a:a**2, squares))
print(fourth_pow)