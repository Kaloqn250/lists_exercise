types_of_fire = input().split('#')
water = int(input())

effort = 0
total_fire_put_out = 0

print('Cells:')
for fire in types_of_fire:
    if 'High' in fire:
        type_of_fire = fire[0:4]
        fire_value = int(fire[6:])
        current_fire = total_fire_put_out
        if 81 <= fire_value <= 125:
            if total_fire_put_out - fire_value <= water:
                water -= fire_value
                effort += fire_value * 0.25
                total_fire_put_out += fire_value
                print(f' - {fire_value}')
    elif 'Medium' in fire:
        type_of_fire = fire[0:6]
        fire_value = int(fire[9:])
        if 51 <= fire_value <= 80:
            if total_fire_put_out - fire_value <= water:
                water -= fire_value
                effort += fire_value * 0.25
                total_fire_put_out += fire_value
                print(f' - {fire_value}')
    elif 'Low' in fire:
        type_of_fire = fire[0:3]
        fire_value = int(fire[6:])
        if 1 <= fire_value <= 50:
            if total_fire_put_out - fire_value <= water:
                water -= fire_value
                effort += fire_value * 0.25
                total_fire_put_out += fire_value
                print(f' - {fire_value}')

print(f'Effort: {effort:.02f}')
print(f'Total Fire: {total_fire_put_out}')
