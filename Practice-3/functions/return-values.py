def maxVal(values):
    maxNum = 0
    max_index = 0
    for i in range(len(values)):
        if values[i] > maxNum:
            maxNum = values[i]
            max_index = i+1
    return maxNum, max_index

nums = list(map(int, input().split()))
maxNum, max_index = maxVal(nums)
print(f"The greatest value is {maxNum}, it's fisrt appearance was on position {max_index}")

def isPresent(word, sentence):
    if word in sentence:
        return True
    else:
        return False

word = input()
phrase = input()
res = isPresent(word, phrase)
print(res)

def buildEvenList():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    evenList = []
    for num in nums:
        if num%2 == 0:
            evenList.append(num)
    return evenList

res = buildEvenList()
for i in range(len(res)):
    print(res[i], end = " ")
print()

def perimeter(a, b, /, *, c, d):
    return a + b + c + d
P = perimeter(6, 7, c = 6, d = 7)
print(P)