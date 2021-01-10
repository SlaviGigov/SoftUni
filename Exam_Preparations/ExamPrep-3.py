def CastSpell(name, power, victim):
    if heroes[name][1] >= int(power):
        heroes[name] = heroes[name][0], heroes[name][1] - int(power)
        return print(f"{name} has successfully cast {victim} and now has {heroes[name][1]} MP!")
    else:
        return print(f"{name} does not have enough MP to cast {victim}!")

def TakeDamage(attacker, power, victim):
    heroes[victim] = heroes[victim][0] - int(power), heroes[victim][1]
    if heroes[victim][0] > 0:
        return print(f"{victim} was hit for {power} HP by {attacker} and now has {heroes[victim][0]} HP left!")
    else:
        heroes.pop(victim)
        return print(f"{victim} has been killed by {attacker}!")

def Recharge(name, power):
    if heroes[name][1] + int(power) > 200:
        used = 200 - heroes[name][1]
        heroes[name] = heroes[name][0], 200
        return print(f"{name} recharged for {used} MP!")
    else:
        heroes[name] = heroes[name][0], heroes[name][1] + int(power)
        return print(f"{name} recharged for {power} MP!")

def Heal(name, power):
    if heroes[name][0] + int(power) > 100:
        used = 100 - heroes[name][0]
        heroes[name] = 100, heroes[name][1]
        return print(f"{name} healed for {used} HP!")
    else:
        heroes[name] = heroes[name][0] + int(power), heroes[name][1]
        return print(f"{name} healed for {power} HP!")

heroes = {}
for n in range(int(input())):
    name, HP, MP = input().split()
    heroes[name] = int(HP), int(MP)

do = input()
while not do == "End":
    if do[0] == "T":
        action, victim, power, attacker = do.split(" - ")
        TakeDamage(attacker, power, victim)
    elif do[0] == "C":
        action, name, power, victim = do.split(" - ")
        CastSpell(name, power, victim)
    elif do[0] == "R":
        action, name, power = do.split(" - ")
        Recharge(name, power)
    elif do[0] == "H":
        action, name, power = do.split(" - ")
        Heal(name, power)
    do = input()

s_heroes = sorted(heroes.items(), key = lambda x:(-x[1][0], x[0]))

for hero in s_heroes:
    print(hero[0])
    print(f"  HP: {hero[1][0]}")
    print(f"  MP: {hero[1][1]}")