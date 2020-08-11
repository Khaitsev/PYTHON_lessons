# 1.Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# https://drive.google.com/file/d/1YMrq2BbTO1U_PhihZM7f9wK8ElzI3WI_/view?usp=sharing - ссылка на диск


number = int(input('Введите любое трехзначное число: '))
number_sum = (number // 100) + ((number // 10) % 10) + (number % 10)
print(number_sum)

number_mul = (number // 100) * ((number // 10) % 10) * (number % 10)
print(number_mul)

