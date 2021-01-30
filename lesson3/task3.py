# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(*args):
    """
    Принимает любое количество аргументов (в том числе три)
    и возвращает сумму наибольших двух из них
    :param args: list любое количество аргументов
    :return:float
    """
    return sum(get_max_from_list(list(args), 2))


def get_max_from_list(number_list, number_count=1):
    """
    Получить максимальные элементы из списка
    :param number_list: list
    :param number_count: int (по-умолчанию 1)
    :return: list
    """

    # если передали список с количество, меньшим,
    # чем нужно максимальных значений - вернем исходный
    if len(number_list) <= number_count:
        return number_list

    max_values = sorted(number_list, reverse=True)[0:number_count]

    return max_values


print(my_func(100, 50, 200))
print(my_func(1, 2, 3))
print(my_func(1000, 100, 1))
