def siblings(*kids):
    print(f"The second oldest child is {kids[1]}")
siblings("A", "B", "C")

def whatsArgs(*args):
    print("Type:", type(args))
    print("First arg:", args[0])
    print("All args:", args)

whatsArgs("Emil", "Tobias", "Linus")

def greetings(greet, *names):
    for name in names:
        print(f"{greet}, {name}. Nice to seeeee you")

greetings("HIIIII" ,"Misha", "Borya", "Aqnaz")

def findMax(*nums):
    maxNum = 0
    for num in nums:
        if num>maxNum:
            maxNum = num
    return maxNum
print(findMax(3, 7, 8, 5, 6, 0, 2, 9))

def info(username, **details):
    print("Username:", username)
    print("Additional info:")
    for key, value in details.items():
        print(" ", key + ":", value)

info("yeet", age = 20, city = "Almaty")
