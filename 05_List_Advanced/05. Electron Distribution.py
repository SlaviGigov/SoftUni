number_of_electrons = int(input())
electrons = []
cell_number = 1

while number_of_electrons > 0:
    possible_electrons = 2*cell_number**2
    if possible_electrons <= number_of_electrons:
        electrons.append(possible_electrons)
    else:
        electrons.append(number_of_electrons)
    number_of_electrons -= possible_electrons
    cell_number += 1


print(electrons)