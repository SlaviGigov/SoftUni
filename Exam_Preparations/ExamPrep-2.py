import re

for n in range(int(input())):
    data = input()
    pattern = r"@#+([A-Z][A-Za-z0-9]+[A-Z])@#+"
    match = re.findall(pattern, data)
    if match == []:
        print(f"Invalid barcode")
    elif len(match[0]) >= 6:
        code = ""
        nums = re.findall("\d", match[0])
        code = "".join(nums)
        if code == "":
            code = "00"
        print(f"Product group: {code}")
    else:
        print(f"Invalid barcode")

#100/100 Many mistakes, the Regex is not bounded, if/elif is not precise