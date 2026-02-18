def silly_function(name = "friend"):
    print(f"I do nothing, {name}...")

ans = input("Do you want me to do nothing? Yes/no ")
if ans.lower() == "yes":
    silly_function()
else:
    name = input("What's your name by the way? ")
    print("Okay! But", end = " ")
    silly_function(name)


def smartFunction(a, b):
    return (a+b)*2


a, b = map(int, input("Give me a and b ").split())
p = smartFunction(a, b)

print(f"If you had a rectangle, its perimeter would be {p}. You're welcome")

# a placeholder
def _hereCouldBe_yourFunction():
    pass