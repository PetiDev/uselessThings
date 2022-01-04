from random import randint

minNum = 1
maxNum = 50

num = randint(minNum, maxNum)
turn = 3
tipp = ""

print(f"Gondoltam egy számra {minNum} és {maxNum} között")

while (tipp != num) and (turn > 0):
    tipp = int(input(f"Tippelj <maradt:{turn}>>"))
    if tipp > num:
        print("A gondolt szám kisebb")
    elif tipp < num:
        print("A gondolt szám nagyobb")

    turn -= 1
else:
    if turn > 0:
        print("Eltaláltad")
    else:
        print("Vesztettél")
