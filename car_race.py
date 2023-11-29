total_times = [int(digit) for digit in input().split()]

middle_index = len(total_times) // 2
left_part = total_times[0:middle_index]
right_part = total_times[middle_index + 1:]
right_part = reversed(right_part)

left_total_time = 0
right_total_time = 0
for left_time in left_part:
    if left_time == 0:
        left_total_time *= 0.8
    left_total_time += left_time

for right_time in right_part:
    if right_time == 0:
        right_total_time *= 0.8
    right_total_time += right_time

if left_total_time < right_total_time:
    print(f'The winner is left with total time: {left_total_time:.01f}')
else:
    print(f'The winner is right with total time: {right_total_time:.01f}')
