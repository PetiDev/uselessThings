from os import system

maxNum = int(input("Input max number> "))
numList = {}
out = ""

print("Generating list...")


for x in range(2, maxNum + 1):
    numList[x] = x
system('cls')
print("Sorting, may take some time...")
for _, val in list(numList.items()):
    currNum = val
    for key, value in list(numList.items()):
        if currNum in numList:
            if (currNum != value) and value % numList[currNum] == 0:
                del numList[value]
system('cls')
print("Joining numbers, may take some time...")
for num in numList:
    out += str(num) + " "
system('cls')
print(out)
input("PAUSE (press enter to exit)")
