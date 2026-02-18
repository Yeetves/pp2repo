# positional and keyword arguments

def mixing(name, surname, job, age):
    print(f"My name is {name}. If you need a surname it's {surname}. I am a {job}. Yes, I am a {job} at {age}, mind your own business pls")

mixing("Kesha", "Sesha", job = "rapper", age = "45")

# playing with data types
def fixList(broken_list):
    for num in broken_list:
        if num != 0:
            print(num, end=" ")
broken_list = [1, 2, 3, 4, 0, 5, 6, 7, 8, 0, 9, 0, 10]

fixList(broken_list)

print()

def func(songs):
    for author, song in songs.items():
        print(f"Author: {author}, song name: {song}")

songs = {
    "Svidanie": "Rvanye rany",
    "Ivan Dorn": "La Re",
    "Lady Gaga": "G.U.Y"
}

func(songs)

def names():
    return ["Stesha", "Munya", "Vasya", "Petya"]

randomNames = names()
for name in randomNames:
    print(name)

