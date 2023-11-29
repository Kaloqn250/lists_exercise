from sys import maxsize
numbers_as_string = input().split()
numbers_to_remove = int(input())

min_number = maxsize
numbers_as_integer = []

for digit in numbers_as_string:
    numbers_as_integer.append(int(digit))

for num in range(numbers_to_remove):
    remove_index = 0
    for current_index in range(len(numbers_as_integer)):
        current_digit = numbers_as_integer[current_index]
        if current_digit < min_number:
            min_number = current_digit
            remove_index = current_index

    numbers_as_integer.remove(numbers_as_integer[remove_index])
    min_number = maxsize

index = 0
for current_num in numbers_as_integer:
    index += 1
    if index < len(numbers_as_integer):
        print(f'{current_num}, ', end='')
    else:
        print(current_num)

