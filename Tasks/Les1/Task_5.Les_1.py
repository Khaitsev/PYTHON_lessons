print('Задание 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым '
      '\nрезультатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). '
      '\nВыведите соответствующее сообщение. Если фирма отработала с прибылью, '
      '\nвычислите рентабельность выручки (соотношение прибыли к выручке). '
      '\nДалее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.')

revenue = int(input('\nвведите выручку: '))
cost = int(input('\nвведите издержки: '))
profit = int(revenue - cost)
profitability = int(profit / revenue * 100)
workers = 0

if revenue > cost:

    print('\nФирма прибыльна ее рентабильность составляет {}%'.format(profitability))
    workers = int(input('\nвведите количество сотрудников: '))
    print(f'\nИз рассчета прибыли на кол-во сотрудников,\nпоказатель вашего предприятия = {int(profit/workers)} руб/чел')
elif revenue < cost:
    print('\nФирма убыточна')
else:
    print('\nФирма работает в "0"')