numbers_as_string = input().split(', ')
beggars_count = int(input())
numbers_as_integer = []

for digit in numbers_as_string:
    numbers_as_integer.append(int(digit))

total_sum = []
start_index = 0

while start_index < beggars_count:
    current_beggar_sum = 0

    for current_index in range(start_index, len(numbers_as_integer), beggars_count):
        current_beggar_sum += numbers_as_integer[current_index]
    total_sum.append(current_beggar_sum)
    start_index += 1

print(total_sum)
