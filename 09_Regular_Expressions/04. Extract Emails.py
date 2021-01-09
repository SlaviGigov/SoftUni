import re
pattern = r"(^|(?<=\s))[A-Za-z0-9]+[\._-]?[A-Za-z0-9]+@([A-Za-z]+(\-)?[A-Za-z]+)(\.)([A-Za-z]+(\-)?[A-Za-z]+)(((\.)([A-Za-z]+(\-)?[A-Za-z]+))+)?"
data = input()

matches = re.finditer(pattern, data)
for match in matches:
    print(match.group())