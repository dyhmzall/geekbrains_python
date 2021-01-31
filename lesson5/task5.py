"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint
from functools import reduce

numbers = [str(randint(0, 1000)) for i in range(200)]

try:
    with open("task5.txt", "w+", encoding="utf-8") as file:
        file.write(' '.join(numbers))
        file.seek(0)  # установим указатель в начало, чтобы можно было прочитать файл
        lines = file.read()
        print(f"Содержимое файла: {lines}")
        summa = reduce(lambda acc, item: acc + float(item), lines.split(), 0)
        print(f"Сумма числе в файле {summa}")
except (EOFError, FileNotFoundError):
    print("Произошла ошибка ввода-вывода! Запись файла.")
