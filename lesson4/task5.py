"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce


def multi_even_list(prev_value, value):
    return prev_value * value


# первый вариант. Какой лучше?
even_list1 = [el for el in range(100, 1001) if not el % 2]
# вторий вариант
even_list2 = [el for el in range(100, 1001, 2)]

print(even_list1)
print(even_list2)

# Вариант первый (вынесенная функция), какой лучше?
print(reduce(multi_even_list, even_list1))
# Вариант второй (анонимная функция)
print(reduce(lambda acc, x: acc * x, even_list2))
