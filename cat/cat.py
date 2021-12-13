from os import system
from time import sleep

frame = 0
frames = []

for x in range(1,9):
    frames.append(("".join(open("./img000"+str(x)+".txt"))))


length = len(frames)

while True:
    print(frames[frame])
    if frame == length:
        frame = 0
    else:
        frame += 1
    sleep(.04)
    system("cls")
