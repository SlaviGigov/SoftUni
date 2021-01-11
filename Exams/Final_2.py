import re
n = int(input())
pattern = r"^(%|\$)(?P<name>[A-Z][a-z]{2,})(\1)(:\s)\[(?P<n1>\d+)\]\|\[(?P<n2>\d+)\]\|\[(?P<n3>\d+)\]\|$"

for _ in range(n):
    data = input()
    message = "no match"
    matches = re.finditer(pattern,data)
    for match in matches:
        tag = match.group("name")
        n1 = match.group("n1")
        n2 = match.group("n2")
        n3 = match.group("n3")
        message = chr(int(n1)) + chr(int(n2)) + chr(int(n3))
        print(f"{tag}: {message}")

    if message == "no match":
        print("Valid message not found!")

