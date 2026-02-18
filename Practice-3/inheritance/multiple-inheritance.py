class FirstClass:
    def smth1(self):
        print("FirstClass's function")
class SecondClass:
    def smth2(self):
        print("SecondClass's function")

class Union(FirstClass, SecondClass):
    pass

obj = Union()
obj.smth1()
obj.smth2()

# without super() Method Order Resolution defines which function is inherited
class OneC:
    def greet(self):
        print("Hello, I'm OneC")
class TwoC:
    def greet(self):
        print("Hello, I'm TwoC")
class PairC(OneC, TwoC):
    pass

pair1 = PairC()
pair1.greet()

class OneC:
    def greet(self):
        print("Hello, I'm OneC")
        super().greet()
class TwoC:
    def greet(self):
        print("Hello, I'm TwoC")
        super().greet()
class ThreeC(OneC, TwoC):
    def greet(self):
        print("Hello, I'm ThreeC")
        super().greet()
class FourC:
    def greet(self):
        print("Hello, I'm FourC")
class FinalC(ThreeC, FourC):
    pass

obj = FinalC()
obj.greet()

class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")
        super().show()


class C(A):
    def show(self):
        print("C")
        super().show()


class D(B, C):
    pass


d = D()
d.show()
