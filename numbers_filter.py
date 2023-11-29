number_of_lines = int(input())

my_list = []

for _ in range(number_of_lines):
    current_num = int(input())
    my_list.append(current_num)

command_line = input()
filtered_list = []
for checking_num in my_list:
    if command_line == 'even':
        if checking_num % 2 == 0:
            filtered_list.append(checking_num)
    elif command_line == 'odd':
        if checking_num % 2 != 0:
            filtered_list.append(checking_num)
    elif command_line == 'negative':
        if checking_num < 0:
            filtered_list.append(checking_num)
    elif command_line == 'positive':
        if checking_num >= 0:
            filtered_list.append(checking_num)

print(filtered_list)
