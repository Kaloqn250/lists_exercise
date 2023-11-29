events = input().split('|')
energy = 100
coins = 100

opened_bakery = True

for event in events:
    event_items = event.split('-')
    type_of_event = event_items[0]
    order_value = int(event_items[1])
    if type_of_event == 'rest':
        current_energy = energy
        energy += order_value
        if energy > 100:
            energy = 100
        gained_energy = energy - current_energy
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')
    elif type_of_event == 'order':
        if energy - 30 >= 0:
            energy -= 30
            coins += order_value
            print(f'You earned {order_value} coins.')
        else:
            energy += 50
            print('You had to rest!')
    else:
        if coins >= order_value:
            coins -= order_value
            print(f'You bought {type_of_event}.')
        else:
            print(f'Closed! Cannot afford {type_of_event}.')
            opened_bakery = False
            break

if opened_bakery:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
