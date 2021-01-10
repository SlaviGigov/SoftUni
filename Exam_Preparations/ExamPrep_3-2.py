#Activation Keys

key = input()

do = input()
while not do == "Generate":
    command = do.split(">>>")[0]
    if command == "Contains":
        substring = do.split(">>>")[1]
        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print(f"Substring not found!")

    elif command == "Flip":
        what = do.split(">>>")[1]
        start = int(do.split(">>>")[2])
        end = int(do.split(">>>")[3])
        if what == "Upper":
            a = key[:start]
            b = "".join([l.upper() for l in key[start:end]])
            c = key[end:]
            key = a + b + c
            print(key)
        elif what == "Lower":
            a = key[:start]
            b = "".join([l.lower() for l in key[start:end]])
            c = key[end:]
            key = a + b + c
            print(key)

    elif command == "Slice":
        start = int(do.split(">>>")[1])
        end = int(do.split(">>>")[2])
        a = key[:start]
        b = key[end:]
        key = a + b
        print(key)

    do = input()

print(f"Your activation key is: {key}")

# 100/100 list slicing