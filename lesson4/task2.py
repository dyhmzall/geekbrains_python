"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка:
[300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат:
[12, 44, 4, 10, 78, 123].
"""

last_value = None


def compare_with_last(value):
    """
    Функция принимает очередной эелмент, сравнивает его с последним и сохраняет текущий элемент как последний
    :param value: int
    :return: bool
    """

    global last_value
    value_large = False

    if last_value is not None and value > last_value:
        value_large = True

    last_value = value

    return value_large


source = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [el for el in source if compare_with_last(el)]

print(f"Исходный список: {source}")
print(f"Итоговый список: {result}")
