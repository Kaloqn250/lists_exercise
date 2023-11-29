# secret_message = [int(digit) for digit in input().split()]
# secret_text = input()
#
# index = 0
#
# while True:
#     if index == len(secret_message):
#         break
#     sum_of_numbers = 0
#     current_num = str(secret_message[index])
#     if len(current_num) > 2:
#         for number in current_num:
#             sum_of_numbers += int(number)
#
#     if sum_of_numbers > len(secret_text):
#         sum_of_numbers -= len(secret_text)
#
#     if sum_of_numbers == 0:
#         print(secret_text[secret_message[index]], end='')
#         character_to_remove = secret_text[secret_message[index]]
#         secret_text = secret_text.replace(character_to_remove, '')
#     else:
#         print(secret_text[sum_of_numbers], end='')
#         character_to_remove = secret_text[sum_of_numbers]
#         secret_text = secret_text.replace(character_to_remove, '')
#
#     index += 1
# Function to calculate the sum of digits of a number
def sum_of_digits(num):
    return sum(map(int, str(num)))


# Input sequence of numbers and the string
numbers = input().split()
message = input().strip()

result = []

for num in numbers:
    num = int(num)
    index = sum_of_digits(num)

    if index >= len(message):
        index %= len(message)

    result.append(message[index])
    message = message[:index] + message[index + 1:]

print(''.join(result))
