# class is an object constructor, a blueprint for creating objects

class MyClass:
    x = 200

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

objects = [p1, p2, p3]
for obj in objects:
    print(obj.x)

del p1

class Undefined:
    pass
