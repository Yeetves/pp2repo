name1 = 'Misha'
name2 = 'Toma'
continuation = "How are you? I don't even want to ask 'how are you'!"
explotion = 'Get out!'
print('Hello, ', name1, '. Nice to see you!', sep="", end=" ")
print(continuation[:12])

print('Hello, ', name2, ". It's not that nice to see you..", sep="", end = " ")
print(continuation[12:] + " " + explotion.upper())


