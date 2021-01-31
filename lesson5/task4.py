"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
from functools import partial


def translate(string, dictionary):
    """
    Попытался сделать функцию универстальное, массив переводов задается словарем
    :param string: str
    :param dictionary: dict
    :return: str
    """

    for (key, value) in dictionary.items():  # key - слово, которое нужно заменить на value, если в строке есть key
        if string.find(key) >= 0:
            # вырезаем то, что было до и после, а в середину вставляем перевод
            string = string[:string.find(key)] + value + string[len(key):]

    return string


def readFile(fine_name):
    try:
        with open("task4_in.txt", "r", encoding="utf-8") as file:
            return file.readlines()
    except (EOFError, FileNotFoundError):
        print("Произошла ошибка ввода-вывода! Чтение файла.")


def saveFile(fine_name, lines):
    try:
        with open(fine_name, "w", encoding="utf-8") as file:
            file.writelines(lines)
    except (EOFError, FileNotFoundError):
        print("Произошла ошибка ввода-вывода! Запись файла.")


dictionary = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре",
}

# применил функцию partial для закрепления материала, кроме того, тут она идеально подошла
count_dictionary = partial(translate, dictionary=dictionary)

lines = readFile("task4_in.txt")
new_lines = [count_dictionary(line) for line in lines]
saveFile("task4_out.txt", new_lines)
