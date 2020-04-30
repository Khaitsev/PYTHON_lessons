numbers = open('text_4.txt', 'r')
numbers_rus = open('text_4(rus).txt', 'w', encoding='utf-8')
mydict = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
numbers_r = numbers.readlines()
for n in numbers_r:
    b = n.split()
    b[0] = mydict.get(int(b[2]))
    q = ' '.join(b)
    numbers_rus.writelines(f'{q}\n')
numbers_rus = open('text_4(rus).txt', 'r', encoding='utf-8')
numbers.close()
numbers_rus.close()
