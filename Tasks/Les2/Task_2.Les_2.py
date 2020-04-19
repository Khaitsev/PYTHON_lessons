numbers = (input('Введите произвольный ряд чисел: '))

numbers = list(numbers)
print(numbers)
new_numbers = []
n = 0
x = []

while len(numbers) > len(new_numbers):
    if len(numbers) % 2 == 0:
        new_numbers.append(numbers[n + 1])
        new_numbers.append(numbers[n])
        n = n + 2
    elif len(numbers) % 2 != 0:
        x = numbers[-1]
        numbers.pop()
        new_numbers.append(numbers[n + 1])
        new_numbers.append(numbers[n])
        n = n + 2

if bool(x) is True:
    new_numbers.append(x)

print(new_numbers)
