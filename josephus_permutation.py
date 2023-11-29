# numbers = [int(digit) for digit in input().split()]
# check_number = int(input())
#
# executed_numbers = []
# index = 0
# while numbers:
#     index += 1
#     if index > len(numbers):
#         executed_numbers.append(numbers[index - len(numbers) - 1])
#         numbers.pop(index - len(numbers) - 1)
#         index = index - len(numbers)
#     else:
#         if index % check_number == 0:
#             executed_numbers.append(numbers[index - (index // check_number)])
#             numbers.pop(index - (index // check_number))
#
#
# print(executed_numbers)

def josephus_permutation(circle, k):
    result = []
    index = 0

    while len(circle) > 0:
        index = (index + k - 1) % len(circle)
        result.append(circle.pop(index))

    return result

# Input parsing
circle = [int(digit) for digit in input().split()]
k = int(input())

permutation = josephus_permutation(circle, k)
print(f'[{",".join([str(number) for number in permutation])}]')
