"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

try:
    with open("task2.txt", "r", encoding="utf-8") as file:
        # подсчет не пустых строк
        strings = [el.strip() for el in file.readlines() if el.strip() != ""]
        print(f"Количество не пустых строк {len(strings)}")

        # подсчет количества слов в не пустых строках
        lines = [(el, len(el.split())) for el in strings]
        for (el, words) in lines:
            print("В строке ", el, f" количство слов: {words}", sep="'")
except (EOFError, FileNotFoundError):
    print("Произошла ошибка ввода-вывода!")
