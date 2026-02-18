mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

# or implement this in for loop
for f in mytuple:
    print(f)


#create an iterator
class MyNums:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 9:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
myClass = MyNums()
myiter = iter(myClass)

for x in myiter:
    print(x, end = " ")
print()
#generators
def func(max):
    cnt = 1
    while cnt<= max:
        yield cnt
        cnt += 1
create_generator = func(5)
for n in create_generator:
    print(n, end = " ")
print()
squares = (x**2 for x in range(1, 6))
for sq in squares:
    print(sq, end=" ")
print()

total = sum(x*10 for x in range(1, 6))
print(total)
# list comprehension vs generator expression
list_comp = [x**2 for x in range(1, 6)]
print(list_comp)

gen_exp = (x**2 for x in range(1, 6))
print(gen_exp)
print(list(gen_exp))