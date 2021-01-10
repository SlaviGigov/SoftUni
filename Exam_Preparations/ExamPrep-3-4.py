#Star Enigma
import re
n = int(input())
a_planets = []
d_planets = []
pattern = r"@(?P<name>[A-Za-z]+)([^@!:>-]+|):(?P<pop>\d+)([^@!:>-]+|)!(?P<do>[AD])!([^@!:>-]+|)(->)(?P<sol>\d+)"

for _ in range(n):
    planet = ""
    do = ""
    data = input()
    new_data = ""
    matches = re.findall("[s,t,a,r,A,S,T,R]", data)
    num = len(matches)

    for l in data:
        new_l = chr(ord(l)-num)
        new_data += new_l

    matches = re.finditer(pattern, new_data)
    for match in matches:
        planet = match.group("name")
        do = match.group("do")

    if do == "A":
        a_planets.append(planet)
    elif do == "D":
        d_planets.append(planet)

print(f"Attacked planets: {len(a_planets)}")
a_planets.sort()
for p in a_planets:
    print(f"-> {p}")

print(f"Destroyed planets: {len(d_planets)}")
d_planets.sort()
for p in d_planets:
    print(f"-> {p}")

#100/100 - hardest ReGex
