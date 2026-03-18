import re

#functions to search a string for a match

txt = "I love pancakes, cakes and not only smth with cakes"
x = re.findall("cakes", txt) #collects all the occurences of "cakes" into a list
print(x)
no_occur = re.findall("Cheese", txt)
print(no_occur) #empty list

ws = re.search("\s", txt) #searches for white-spaces. X is an object. Returns None if no matches
print(ws)
print(ws.span())
print(ws.start())

splited_list = re.split("\s", txt) #splits at white-spaces and collects into a list
print(splited_list)

kinda_splited = re.split("\s", txt, maxsplit=2) #splits only 2 times
print(kinda_splited)


replaced = re.sub("cakes", "brownies", txt)
print(replaced)

kinda_replaced = re.sub("cakes", "cake", txt, 1) #specify number of replacements
print(kinda_replaced)


#SEARCH RETURNS OBJECTS
txt = "Cats, dogs, monkeys, snakes, elephants, mammals, dinosaurs, I'm done"
x = re.search(r"\bd\w+", txt)
print(x.span()) #prints indexes of characters (start and end+1)
print(x.string) #prints the string that was passed into a function
print(x.group()) #prints the group of characters where match was found

