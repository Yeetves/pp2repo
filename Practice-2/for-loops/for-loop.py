s = "Check my letters"
vowels = ["a", "e", "i", "o", "u", "y"]
consonants = ["q", "w", "r", "t", "p", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]

for letter in s.lower():
    if letter in vowels:
        print(f"{letter} is a vowel")
    elif letter in consonants:
        print(f"{letter} is a consonant")
    else:
        print("It's just a space))")

bad_str = "At some moment I'll break and become unreadable, i'm sorr35493485743856834923582359"

for x in bad_str:
    if x.isdigit():
        break
    print(x, end="")

print()

notThatBad_str = "I'll break too bu3497593458934857t I'll come back!!"
for l in notThatBad_str:
    if l.isdigit():
        continue
    print(l, end="")