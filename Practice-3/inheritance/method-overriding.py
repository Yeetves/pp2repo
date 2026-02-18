import math
class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius**2)
    
rect = Rectangle(10, 20)
circ = Circle(3)
print(rect.area())
print(circ.area())


class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    def get_salary(self):
        return self.base_salary
    
class Manager(Employee):
    def __init__(self, name, base_salary, percent):
        super().__init__(name, base_salary)
        self.percent = percent
    def get_salary(self):
        standard_salary = super().get_salary()
        return standard_salary + self.percent
    
empl = Employee("Boris", 500000)
mang = Manager("Lizo4ka", 500000, 60000)

print(empl.get_salary())
print(mang.get_salary())

class Pet:
    def voice(self):
        pass
class Cat(Pet):
    def __init__(self, name):
        self.name = name
    def voice(self):
        print(f"Meow! Meow namew is {self.name}")
class Dog(Pet):
    def __init__(self, name):
        self.name = name
    def voice(self):
        print(f"Bark! I'm {self.name}")

kis = Cat("Myash")
dogik = Dog("Bobik")

kis.voice()
dogik.voice()