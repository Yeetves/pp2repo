import math

takeMax = max(7, 8, 3, 5, 9, 10, 56)
takeMin = min(5, 2, 3, 1, 8, 7, 4, 456)
print(f"Max value was {takeMax}, min value - {takeMin}")

calculated_error = float(input("What error did you get?"))
allowedError = 2
moduled_error = abs(calculated_error)
if moduled_error <= allowedError:
    print("Your experiment is okay")
else:
    print("you're cooked!")

squares = [pow(x, 2) for x in range(1, 10)]
print(squares)

initial_vals = [math.sqrt(square) for square in squares]

radius = int(input("Give me a random number"))
circArea = math.pi * (radius**2)
print(f"You would have a circle of {circArea} area")

roundedRoots = [math.floor(math.sqrt(x)) for x in range(1, 10)]
print(roundedRoots)
