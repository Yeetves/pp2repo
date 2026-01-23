great = 60
cooked = 29

score = int(input("What's your score for both attestations?"))
print(type(score))

if score > cooked and score <= great:
    print("Great! u've still got hope")
elif score > great or score < 0:
    print("liar.")
else:
    print("you are cooked!")

# this code is secured in case of idiots!!
