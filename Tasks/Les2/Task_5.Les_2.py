numbers = [7, 5, 3, 3, 2, 9]

user_nu = int(input('Введите натуральное число: '))

numbers.append(user_nu)
# еще и развернул
numbers.reverse()

numbers.sort()

print(numbers)
