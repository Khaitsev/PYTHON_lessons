f = open('file.txt', 'a', encoding='utf-8')
while True:
    msg = (input('msg: '))
    if bool(msg) == bool(True):
        f.write(msg + '\n')
    else:
        break
f = open('file.txt', 'r', encoding='utf-8')
print(f.read())
f.close()
