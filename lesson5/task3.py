"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""
from functools import reduce

try:
    with open("task3.txt", "r", encoding="utf-8") as file:

        lines = file.readlines()

        peoples = [el.split()[0] for el in lines if float(el.split()[1]) < 20000]
        print("Сотрудники, которые имеют оклад меньше 20000")
        for (index, people) in enumerate(peoples, 1):
            print(index, people)

        average = reduce(lambda acc, item: acc + float(item.split()[1]), lines, 0) / len(lines)

        print(f"Средняя величина дохода сотрудников составляет {average}")
except (EOFError, FileNotFoundError):
    print("Произошла ошибка ввода-вывода!")
