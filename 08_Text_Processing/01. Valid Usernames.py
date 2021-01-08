data = input().split(", ")

def lenght(name):
    if not 3 <= len(name) <= 16:
        return "Wrong"

def symbols(name):
    for w in name:
        if not (w.isdigit() or w.isalpha() or w == "-" or w == "_"):
            return "Wrong"
        if w == "@" or w == " " or w == "!":
            return "Wrong"

for name in data:
    if not (lenght(name) == "Wrong" or symbols(name) == "Wrong"):
        print(name)
