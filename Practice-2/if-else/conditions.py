a = 10
b = 15

if a < b: print("b is greater than a") # one line if statement

a = 15
print("A is greater") if a > b else print("they are equal..") if a == b else print("b is greater") # multiple conditions in one line

x = 9
y = 8
max_value = x if x > y else y
print(max_value, "is the greatest")

username = "admin"
print("Hi, admin!!!!") if username == "admin" else print(f"Welcome, {username}") if username else print("Who are you..")