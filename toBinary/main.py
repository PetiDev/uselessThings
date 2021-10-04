import math

num1 = int(input("inpunt a number> "))
num2 = 0
num3 = ""

while num1 >= 1:
    num2 = num1 % 2
    num3 += str(num2)
    num1 = math.floor(num1 / 2)

print(num3[::-1])
input("PAUSE (press enter to exit)")
