n = int(input())

if n < 100:
    print(f"{n}% [{'%'*int(n/10)}{'.'*int(10-n/10)}]")
    print("Still loading...")
else:
    print("100% Complete!")
    print("[%%%%%%%%%%]")