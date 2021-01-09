import re
pattern = r"((?<=^_)|(?<=\s_))[A-Za-z0-9]+\b"
result = [el.group() for el in re.finditer(pattern, input())]
print(",".join(result))