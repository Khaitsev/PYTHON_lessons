from sys import argv

name, first_param, second_param, third_param = argv

first_param = int(first_param)
second_param = int(second_param)
third_param = int(third_param)
print("Выработка в часах: ", int(first_param))
print("Ставка в час: ", int(second_param))
print("Премия: ", int(third_param))
total = ((first_param * second_param) + third_param)
print("Зарплата сотрудника: ", total)
