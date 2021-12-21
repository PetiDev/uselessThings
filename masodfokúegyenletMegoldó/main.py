from math import sqrt
import re

print("EPIKUS MÁSODFOKÚEGYENLETSZÁMOLÓ\n\n")


def refactor(tex):
    refactorer = re.search(r"=.*", tex).group()
    tex = re.sub(r"=.*", "= 0", tex)
    refactorer = refactorer[1:]
    refactorer = re.sub(r"@", "-", re.sub(r"-", "+", re.sub(r"\+", "@", refactorer)))
    return refactorer + tex


txt = "+12x^2+24x^2-26x^2+6-9 = +13x"
# txt = input("Adj meg egy egyenletet, ne hagyd le az elejéről a + vagy - jelet mert kell és a számokat se hagyd le akkor se ha csak 1x van> ")

txt = refactor(txt)

a = 0
b = 0
c = 0
selections = [re.findall(r"[-+]?\d+x\^2", txt), re.findall(r"[+-]?\d+x(?=[-+ =])", txt), re.findall(r"[^^]\d+(?=[-+ =])", txt)]

for x in selections[0]:
    a += int(re.search(r"[-+]\d+", x).group())
for x in selections[1]:
    b += int(re.search(r"[+-]?\d+", x).group())
for x in selections[2]:
    c += int(re.search(r"[-+]\d+", x).group())


print("a:", a)
print("b:", b)
print("c:", c)

ans1 = ((-b)+sqrt(b**2-4*a*c))/(2*a)
ans2 = ((-b)-sqrt(b**2-4*a*c))/(2*a)
print("Ans1:", ans1, "\nAns2:", ans2)
