numbers = [7, 5, 3, 3, 2]
print(numbers)
user_nu = int(input('Введите натуральное число: '))
numbers.append(user_nu)

numbers.sort()
print(numbers)

# или, если нельзя sort и reverse

numbers = [7, 5, 3, 3, 2]
user_nu = int(input('Введите натуральное число: '))
print(numbers)
print(bool(numbers.count(user_nu)))

if numbers.count(user_nu) == 1:
    numbers.insert(numbers.index(user_nu), user_nu)

elif numbers.count(user_nu) > 1:
    numbers.insert((numbers.index(user_nu)) + numbers.count(user_nu), float(user_nu))

elif numbers.count(user_nu) < 1:
    for n in numbers:
        if n == numbers[-1]:
            numbers.append(float(user_nu))
            break
        elif user_nu > n:
            numbers.insert(numbers.index(n), float(user_nu))
        elif user_nu < n:
            continue

        break

print(numbers)
