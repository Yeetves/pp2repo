class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)

class Drummer(Person):
    def __init__(self, fname, lname, group):
        super().__init__(fname, lname)
        self.group = group
    def welcome(self):
        print(f"Welcome, {self.firstname} {self.lastname} from {self.group}")

art1 = Drummer("Jonas", "Jordison", "Slipknot")
art1.welcome()

class Singer(Person):
    def __init__(self, fname, lname, country):
        super().__init__(fname, lname)
        self.country = country
    def get_profile(self):
        return f"{self.firstname} {self.lastname} is a singer from {self.country}"

singer1 = Singer("Sabrina", "Carpenter", "US")
print(singer1.get_profile())
