def user_data(name, l_name, bd, city, email, t_number):
    u_d = {'name': name, 'last name': l_name, 'date of birth': bd, 'city': city, 'e-mail': email,
           'phone number': t_number}
    return u_d


print(user_data(input("Введите имя: "), input("Введите фамилию: "), input("Введите дату рождения: "),
                input("Введите город: "), input("Введите E-mail: "), input("Введите телефон: ")))
