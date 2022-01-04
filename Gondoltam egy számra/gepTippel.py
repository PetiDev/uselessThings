from random import randint

maxNum = 50
minNum = 0
tipp = ""
turn = 10


for _ in range(turn):
    tipp = randint(minNum, maxNum)
    print(f"A tipp: {tipp}")
    ans = input("A gondolt szám Nagyobb vagy kisebb esetleg eltalálta?").lower()
    if (ans == "nagyobb") or (ans == "n"):
        minNum = int(tipp) + 1
    elif (ans == "kisebb") or (ans == "k"):
        maxNum = int(tipp) - 1
    elif (ans == "eltaláltad") or (ans == "e"):
        print("JEEEEEEJ")
        break

else:
    print("Nyertél")
