qty = int(input('Введите количеств позиций: '))
total = {
    "название": [],
    "цена": [],
    "количество": [],
    "ед": []
}
items = []

for n in range(qty):
    item = input(f'Введите наименование {n + 1} товара: ')
    total["название"].append(item)
    item_price = input(f'Введите цену {item}(-а) за ед.: ')
    total["цена"].append(item_price)
    item_qty = input(f'Введите количество {item}(-ов): ')
    total['количество'].append(item_qty)
    item_meas = input(f'Введите единицу измерения {item} (шт,ед,кг..)')
    total['ед'].append(item_meas)
    items.append((n + 1, {"название": item, "цена": item_price, "количество": item_qty, "eд": item_meas}))

print(items)
print(total)