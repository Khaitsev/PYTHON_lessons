workers = open('text_3.txt', 'r', encoding='utf-8')
wrk = workers.readlines()
w_dict = {}
qty = 0
less20qty = 0
total_sum = 0
less20sum = 0
for n in wrk:
    w = []
    w.append(n.split())
    w_dict[w[0][0]] = int((w[0][1])[:-2])

for n, m in w_dict.items():
    qty += 1
    total_sum = total_sum + m
    if m <= 20000:
        less20sum = less20sum + m
        less20qty += 1
        print(n, m)

print(f'Средняя зарплата всех сотрудников в комании: {int(total_sum / qty)}')
print(f'Средняя зарплата сотрудников, чьи оклады меньше 20к: {int(less20sum / less20qty)}')

workers.close()
