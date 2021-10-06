from os import system

maxNum = int(input("Input max number> "))
numList = {}
out = ""

print("Generating list...")
system('cls')

for x in range(2, maxNum + 1):
    numList[x] = x

for _, val in list(numList.items()):
    currNum = val
    for key, value in list(numList.items()):
        if currNum in numList:
            if (currNum != value) and value % numList[currNum] == 0:
                del numList[value]

for num in numList:
    out += str(num) + " "

print(out)
input("PAUSE (press enter to exit)")
