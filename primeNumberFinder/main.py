from os import system

maxNum = int(input("Input max number> "))
numList = {2: 2}
out = ""

print("Generating list...")

# Generating number list
for x in range(3, maxNum + 1, 2):
    numList[x] = x

system('cls')
print("Sorting, may take some time...")

# Sorting prime numbers from list
for _, val in list(numList.items()):
    currNum = val
    for key, value in list(numList.items()):
        if currNum in numList:
            if (currNum != value) and value % numList[currNum] == 0:
                del numList[value]
system('cls')
print("Joining numbers, may take some time...")
# Joining output string
for num in numList:
    out += str(num) + " "
system('cls')
print(out)
input("PAUSE (press enter to exit)")
