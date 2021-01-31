"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
from random import randint
from functools import reduce
from json import dump


def get_firm_data(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            # составим словать с названиями фирм и прибылью (минус значит убыток)
            firms = {el.split()[0]: float(el.split()[2]) - float(el.split()[3]) for el in file.readlines()}
            # вычислить среднюю прибыль
            profit_summa = reduce(lambda acc, x: acc + x if x > 0 else acc, firms.values(), 0)
            profit_count = reduce(lambda acc, x: acc + 1 if x > 0 else acc, firms.values(), 0)
            result = [firms, {"average_profit": round(profit_summa / profit_count, 2)}]
            return result
    except (EOFError, FileNotFoundError):
        print("Ошибка чтения исходного файла!")
        exit()


def save_json(file_name, data):
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            dump(data, file)
    except (EOFError, FileNotFoundError):
        print("Ошибка записил JSON в файл!")
        exit()


def make_source_file():
    """
    хоть файл не нужно генерировать программно, но придумывать лениво)
    """
    try:
        with open("task7.txt", "w", encoding="utf-8") as file:
            for i in range(1, 26):
                firm_name = f"firm_{i:02}"
                firm_form = "OOO" if i % 2 else "OAO"
                firm_proceeds = randint(500000, 1000000)
                firm_costs = randint(100000, 1000000)
                file.write(f"{firm_name} {firm_form} {firm_proceeds} {firm_costs}\n")
    except (EOFError, FileNotFoundError):
        print("Ошибка формирования исходного файла!")
        exit()


# закомментировать, если не нужно генерировать файл
make_source_file()

data = get_firm_data("task7.txt")
print(data)
save_json("task7.json", data)
