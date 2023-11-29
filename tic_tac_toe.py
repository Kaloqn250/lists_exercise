first_line = [int(digit) for digit in input().split()]
second_line = [int(digit) for digit in input().split()]
third_line = [int(digit) for digit in input().split()]

for i in range(len(first_line)):
    for j in range(len(second_line)):
        if first_line[i] == second_line[j]:
            for k in range(len(third_line)):
                if second_line[j] == third_line[k]:
                    if first_line[i] == 1:
                        print('First player win')
                        break
                    elif first_line[i] == 2:
                        print('Second player win')
                        break
            break
    break

