initial_list = input().split("!")
command = input()

while not command == "Go Shopping!":
    list_of_command = command.split()
    if list_of_command[0] == "Urgent" and list_of_command[1] not in initial_list:
        initial_list.insert(0, list_of_command[1])
    if list_of_command[0] == "Unnecessary" and list_of_command[1] in initial_list:
        initial_list.remove(list_of_command[1])
    if list_of_command[0] == "Correct" and list_of_command[1] in initial_list:
        n = initial_list.index(list_of_command[1])
        initial_list.remove(list_of_command[1])
        initial_list.insert(n, list_of_command[2])
    if list_of_command[0] == "Rearrange" and list_of_command[1] in initial_list:
        initial_list.remove(list_of_command[1])
        initial_list.append(list_of_command[1])
    command = input()

print(", ".join(initial_list))