# 2022, 03. 29.
from random import choice

table = {
    "A1": "0", "A2": "0", "A3": "0", "A4": "0", "A5": "0",
    "B1": "0", "B2": "0", "B3": "0", "B4": "0", "B5": "0",
    "C1": "0", "C2": "0", "C3": "0", "C4": "0", "C5": "0",
    "D1": "0", "D2": "0", "D3": "0", "D4": "0", "D5": "0",
    "E1": "0", "E2": "0", "E3": "0", "E4": "0", "E5": "0"
}
ingame = True
target = choice(list(table.keys()))
round = 0

while ingame:
    round += 1
    print(f"*************[ {round}. kör ]*************")
    print(f"   A  B  C  D  E"
          f"\n1 [{table['A1']}][{table['A2']}][{table['A3']}][{table['A4']}][{table['A5']}]"
          f"\n2 [{table['B1']}][{table['B2']}][{table['B3']}][{table['B4']}][{table['B5']}]"
          f"\n3 [{table['C1']}][{table['C2']}][{table['C3']}][{table['C4']}][{table['C5']}]"
          f"\n4 [{table['D1']}][{table['D2']}][{table['D3']}][{table['D4']}][{table['D5']}]"
          f"\n5 [{table['E1']}][{table['E2']}][{table['E3']}][{table['E4']}][{table['E5']}]")
    guess = input("Kérem a koordinátákat a tüzeléshez>>").upper()

    if guess == target:
        print("Találaaaaat! **Hurráááááá hurrááááááá...**")
        table[guess] = "BOOM"
        ingame = False
    else:
        table[guess] = "x"
        print("Sajnos a torpedó nem talált célba!\n tüzelj újra\n")
input("press ENTER to exit")
