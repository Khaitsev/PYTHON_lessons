from itertools import count, cycle

for n in count(1):
    print(n)
    if n >= 30:
        break
a = 1
for n in cycle("123"):
    print(n)
    a += 1
    if a == 10:
        break
