"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

try:
    with open("task1.txt", "w", encoding="utf-8") as file:
        while True:
            string = input("Введите строку для записи в файл: ")
            if string == "":
                break
            else:
                file.write(string + "\n")
except (EOFError, FileNotFoundError):
    print("Произошла ошибка ввода-вывода!")
