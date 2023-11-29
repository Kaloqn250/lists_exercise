factor = int(input())
count = int(input())
my_list = []

for current_num in range(1, count + 1):
    my_list.append(current_num * factor)

print(my_list)