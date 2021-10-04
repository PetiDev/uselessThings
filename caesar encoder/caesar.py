"""
színekkel:
print("\033[95m     Készítette: \033[4mHorváth Péter\033[0m\n\033[94mCaesar kódoló Ascii táblázat alapon.\033[0m\n")
"""
print("     Készítette: Horváth Péter\nCaesar kódoló Ascii táblázat alapon.\n")

text = ""
key = ""
out = ""

textList = {}
keyList = {}
outList = {}
counter = 0

while text == "":
    text = input("Adj meg egy szöveget> ")
while key == "":
    key = input("Adj meg egy kulcsot> ")

mode = input("Adj meg egy módot (encode/decode;e/d){def: encode}> ").lower()

while len(key) < len(text):
    key += key

for letter in text:
    textList[counter] = ord(letter)
    counter += 1
counter = 0

for letter in key:
    keyList[counter] = ord(letter) - 64
    counter += 1
counter = 0

if mode == "decode" or mode == "d":
    for x in range(len(key)):
        outList[x] = textList[x] - keyList[x]
else:
    for x in range(len(key)):
        outList[x] = textList[x] + keyList[x]

for x in range(len(outList)):
    out += chr(outList[x])

print("Eredmény:", out)
input("PAUSED (hit enter to exit)")
