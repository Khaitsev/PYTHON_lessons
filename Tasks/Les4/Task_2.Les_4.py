my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

my_list2 = [n for n in my_list if n > my_list[my_list.index(n) - 1] and my_list.index(n) != 0]
print(my_list2)

