all_gifts = input().split()

command_line = input()

while command_line != 'No Money':
    if 'OutOfStock' in command_line:
        gift = command_line[11:]

        for index in range(len(all_gifts)):
            if gift == all_gifts[index]:
                all_gifts[index] = 'None'
    elif 'Required' in command_line:
        gift, index = command_line[9:].split()
        int_index = int(index)
        if 0 <= int_index <= len(all_gifts) - 1:
            all_gifts[int(index)] = gift
    elif 'JustInCase' in command_line:
        all_gifts[-1] = command_line[11:]

    command_line = input()

for word in all_gifts:
    if word != 'None':
        print(word, end=' ')
