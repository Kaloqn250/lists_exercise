numbers = list(map(int, input().split(', ')))

sorted_numbers = []
for current_num in numbers:
    if current_num != 0:
        sorted_numbers.append(current_num)
for number in numbers:
    if number == 0:
        sorted_numbers.append(number)

print(sorted_numbers)
