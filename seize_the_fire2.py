types_of_fire = input().split('#')
water = int(input())

effort = 0
total_fire_put_out = 0

print('Cells:')
for fire in types_of_fire:
    type_of_event = fire.split('=')
    type_of_fire = type_of_event[0]
    fire_value = int(type_of_event[1])
    if 'High' in fire:
        current_fire = total_fire_put_out
        if 81 <= fire_value <= 125:
            current_fire -= fire_value
            if current_fire <= water:
                water -= fire_value
                effort += fire_value * 0.25
                total_fire_put_out += fire_value
                print(f' - {fire_value}')
    elif 'Medium' in fire:
        current_fire = total_fire_put_out
        if 51 <= fire_value <= 80:
            current_fire -= fire_value
            if current_fire <= water:
                water -= fire_value
                effort += fire_value * 0.25
                total_fire_put_out += fire_value
                print(f' - {fire_value}')
    elif 'Low' in fire:
        current_fire = total_fire_put_out
        if 1 <= fire_value <= 50:
            current_fire -= fire_value
            if current_fire <= water:
                water -= fire_value
                effort += fire_value * 0.25
                total_fire_put_out += fire_value
                print(f' - {fire_value}')

print(f'Effort: {effort:.02f}')
print(f'Total Fire: {total_fire_put_out}')

