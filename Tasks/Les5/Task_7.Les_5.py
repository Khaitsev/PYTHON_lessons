from functools import reduce
import json

f = open('text_7.txt', 'r', encoding='utf-8')
file = f.readlines()
comp = {}
for n in file:
    spl = n.split()
    if int(spl[2]) > int(spl[3]):
        pr = int(spl[2]) - int(spl[3])
        comp[spl[0]] = int(pr)
# потренил reduce
av_profit = {'average_profit': reduce(lambda x, y: x + y, comp.values()) / len(comp.values())}

json_f = [comp, av_profit]
print(json_f)

with open('text_77.json', 'w+', encoding='utf-8') as j:
    json.dump(json_f, j, ensure_ascii=False, indent=4)
    j.seek(0)
    x = j.read()
    print(x)

# проверка
print(sum(comp.values()) / len(comp.values()))
f.close()
