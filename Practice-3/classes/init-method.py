class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

c1 = Cat("Barsik", 1)
print(f"{c1.name}, {c1.age} years old")

c2 = Cat("Murzik", 4)
c3 = Cat("Barbos", 2)

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def bark(self):
        print(f"I am {self.name}")

    def greet(self):
        print(f"Hey, I am {self.name}, {self.breed}. I'm {self.age} years old.")
dog1 = Dog("Bobrik", 2, "mops")
dog2 = Dog("Barbos", 6, "dolmatin")

dog1.bark()
dog2.greet()

class Person:
    def __init__(info, name, sex, profession):
        info.name = name
        info.sex = sex
        info.profession = profession
    def display_info(info):
        print(f"{info.name}, {info.sex}, {info.profession}")

p1 = Person("Adil", "male", "traktorist")
p1.display_info()
