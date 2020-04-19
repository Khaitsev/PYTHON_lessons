words = input('Введите 3-5 слов с пробелами: ')

split_words = words.split(' ')
step = 1
print(split_words)

for n in split_words:
    print(step, n[:10])
    step += 1
