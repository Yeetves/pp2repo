cats = [("Barbos", 1), ("Pushok", 5), ("Murzik", 3), ("Barsik", 2)]
sorted_cats = sorted(cats, key = lambda x : x[0])
print(sorted_cats)

sorted_cats = sorted(cats, key = lambda x : x[1])
print(sorted_cats)

cats = ["Barbos", "Belka", "Ryzhyik", "Barsik"]
sorted_cats = sorted(cats, key = lambda x: len(x))
print(sorted_cats)

nums = [7, 9, 4, 5, 2, 8, 0, 3 ,1, 6, 7, 4]
sorted_nums = sorted(nums, key = lambda x : x )
print(sorted_nums)

