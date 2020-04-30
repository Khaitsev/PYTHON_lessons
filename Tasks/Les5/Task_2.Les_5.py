f = open('file.txt', 'r', encoding="utf - 8")
a = 0
for n in f:
    a += 1
    x = []
    x.append(n.split())
    for q in x:
        b = len(q)
    print(f'в строке {a}: {b} слов(-а)')

# второй вариант
print(f.tell())
f.seek(0)
print(f.tell())
z = f.readlines()
s = 0
for b in z:
    s += 1
    print(f'в строке {s}: {len(b.split())} слов(-а)')
f.close()
