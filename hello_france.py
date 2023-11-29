items_list = input().split('|')
budget = int(input())

profit_checker = budget
bought_items = []
sold_items_value = 0

for item in items_list:
    if 'Clothes' in item:
        item_value = float(item[9:])
        if item_value <= 50:
            if budget >= item_value:
                bought_items.append(item_value)
                budget -= item_value
    elif 'Shoes' in item:
        item_value = float(item[7:])
        if item_value <= 35:
            if budget >= item_value:
                bought_items.append(item_value)
                budget -= item_value
    elif 'Accessories' in item:
        item_value = float(item[13:])
        if item_value <= 20.50:
            if budget >= item_value:
                bought_items.append(item_value)
                budget -= item_value
for current_item in bought_items:
    selling_item = current_item + (current_item * 0.40)
    sold_items_value += selling_item
    print(f'{selling_item:.02f}', end=' ')

print()
profit = sold_items_value - profit_checker + budget
print(f'Profit: {profit:.02f}')
sold_items_value += budget
if sold_items_value >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
