my_list = []

for _ in range(3):
    input_line = input()

    my_list.append(input_line)

my_list[0], my_list[2] = my_list[2], my_list[0]

print(my_list)
