# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

any_type_list = list()

any_type_list.append(None)
any_type_list.append(True)
any_type_list.append(1)
any_type_list.append(3.14)

any_type_list.extend(['first_string', 'second_string', 'third_string'])

any_type_list.extend([[1, 2, 3], ['one', 'two', 'three']])  # списки
any_type_list.extend([(1, 2, 3), ('one', 'two', 'three')])   # кортежи
any_type_list.extend([{1, 3, 5, 7, 9}, {'he', 'she', 'it'}])  # множества

any_type_list.append({1: 2, 'three': 4, 5: 6, 7.5: 8, 9: 'zero'})  # словарь

for any_type_element in any_type_list:
    if type(any_type_element) == type(None):
        type_element = 'тип None'
    elif type(any_type_element) == bool:
        type_element = 'тип BOOL'
    elif type(any_type_element) == int:
        type_element = 'тип INT'
    elif type(any_type_element) == float:
        type_element = 'тип FLOAT'
    elif type(any_type_element) == str:
        type_element = 'тип STR'
    elif type(any_type_element) == list:
        type_element = 'тип LIST'
    elif type(any_type_element) == tuple:
        type_element = 'тип TUPLE'
    elif type(any_type_element) == set:
        type_element = 'тип SET'
    elif type(any_type_element) == dict:
        type_element = 'тип DICT'
    else:
        type_element = 'тип неопределен'

    print(any_type_element, end=' ')
    print(type_element)
