days = int(input())
per_day = int(input())
expected = int(input())
gathered = 0
the_day = 0

while the_day < days:
    the_day += 1
    gathered += per_day
    if the_day % 3 == 0:
        gathered += per_day*0.5
    if the_day % 5 == 0:
        gathered = gathered*0.7

if gathered >= expected:
    print(f"Ahoy! {gathered:.2f} plunder gained.")
else:
    print(f"Collected only {(gathered/expected*100):.2f}% of the plunder.")