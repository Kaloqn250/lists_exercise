numbers_as_string = input().split()
opposite_list = []
for digit in numbers_as_string:
    current_num = -int(digit)
    opposite_list.append(current_num)

print(opposite_list)
