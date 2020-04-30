my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

my_list2 = [n for n in my_list if my_list.count(n) < 2]
print(my_list2)