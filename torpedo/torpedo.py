from random import randint, choice


def genTable(size):
    global table
    table = [["0" for i in range(size)] for j in range(size)]
    global target
    target = {
        "x": randint(1, len(table))-1,
        "y": randint(1, len(table))-1
    }


def draw():
    canvas = ""
    count = 1
    canvas += f"  {' '.join(letterMap[0:len(table)])}\n"
    for row in table:
        canvas += f"{count} {'|'.join(row)}\n"
        count += 1
    print(canvas)


def place(xy):
    x = xy[0]
    y = int(xy[1::])
    x = letterMap.index(x)
    y -= 1

    if x == target["x"] and y == target["y"]:
        print("!!!Találat!!!")
        global inGame
        inGame = False
    else:
        print("nem talált, talán legközelebb")
        table[y][x] = "X"


target = {}
inGame = True
turn = 0
letterMap = "abcdefghijklmnopqrstuvwxyz"


while inGame:

    turn += 1
    print(f"*****[kör: {turn}]*****")

    if turn == 1:
        genTable(int(input("mekkora legyen a tábla 1-26?")))

    draw()
    place(input("Add meg a mezőt pl: A1>>").lower())

