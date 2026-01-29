age = int(input("How old are you?)"))
hasJob = input("Do you have a job?")
isGood = False
if hasJob.lower() == 'yes':
    isGood = True

if age < 18:
    print("Don't listen to me, just enjoy your life..")
elif age >= 18 and age < 25:
    if isGood:
        print("Wow! U'r doing so great")
    else:
        print("Don't worry, you need some time")
else:
    if isGood:
        print("Undoubtedly, you don't have other choices")
    else:
        print("Just shame on u.")
