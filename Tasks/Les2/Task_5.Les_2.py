numbers = [7, 5, 3, 3, 2]
print(numbers)
user_nu = int(input('Введите натуральное число: '))
numbers.append(user_nu)
# еще и развернул
numbers.reverse()
numbers.sort()
print(numbers)

# или, если нельзя sort и reverse

numbers = [7, 5, 3, 3, 2]
user_nu = int(input('Введите натуральное число: '))
print(numbers)
print(bool(numbers.count(user_nu)))

if numbers.count(user_nu) == 1:
    numbers.insert(numbers.index(user_nu), user_nu)
elif numbers.count(user_nu) < 1:
    numbers.append(user_nu)
elif numbers.count(user_nu) > 1:
    numbers.insert((numbers.index(user_nu) - 1) + numbers.count(user_nu), user_nu)

print(numbers)
