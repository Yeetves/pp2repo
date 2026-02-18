class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)

x = Person("Ron", "Weasley")
x.printname()

class Musician(Person):
    pass

x = Musician("Jonas", "Jordison")
x.printname()

class Artist(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)