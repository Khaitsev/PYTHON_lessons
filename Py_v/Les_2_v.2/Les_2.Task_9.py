# 9.Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


numbers = '1, 343, 4354, 1235, 46754, 345, 1432, 4561, 8523, 32, 4265'
max_n = 0
sum_mux_n = 0

for n in numbers.split(', '):
    if int(n) > max_n:
        max_n = int(n)
for n in str(max_n):
    sum_mux_n += int(n)

print(max_n)
print(sum_mux_n)
