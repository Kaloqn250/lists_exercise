numbers_of_lines = int(input())
key_word = input()

my_list = []

for _ in range(numbers_of_lines):
    input_line = input()

    my_list.append(input_line)

filtered_list = []
for check_line in my_list:

    if key_word in check_line:
        filtered_list.append(check_line)

print(my_list)
print(filtered_list)