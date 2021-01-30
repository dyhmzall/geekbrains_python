# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def print_user(name, surname, birth_date, city, email, phone):
    """
    Выводит данные пользователя
    :param name: string
    :param surname: string
    :param birth_date: string
    :param city: string
    :param email: string
    :param phone: string
    :return:
    """
    print(f"{name} {surname} <{email}> ({phone}), {city}, дата рождения: {birth_date}, ")


# позиционные параметры
print_user("Михаил", "Поправко", "31.08.1988", "Брянск", "dyhmzall@gmail.com", "+7950693**32")

# именованные параметры по порядку
print_user(name="Михаил", surname="Поправко", birth_date="31.08.1988",
           city="Брянск", email="dyhmzall@gmail.com", phone="+7950693**32")

# именованные параметры НЕ по порядку
print_user(phone="+7950693**32", email="dyhmzall@gmail.com", city="Брянск",
           birth_date="31.08.1988", surname="Поправко", name="Михаил")
