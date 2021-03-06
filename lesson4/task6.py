"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
from itertools import count, cycle


def get_numbers_from(from_value):
    for el in count(from_value):
        if el > 10:  # при достижении числа 10 завершаем цикл
            break
        else:
            yield el


def get_duplicate_for(source_list):
    for index, el in enumerate(cycle(source_list)):
        if index > len(source_list) - 1:  # повторение элементов списка будет прекращено
            break
        else:
            yield el


print("Итератор, генерирующий целые числа, начиная с указанного")
for el in get_numbers_from(3):
    print(el)

print("Итератор, повторяющий элементы некоторого списка, определенного заранее")
for el in get_duplicate_for([1, 2, 3, 4, 5, 6, 7, 8, 9]):
    print(el)
