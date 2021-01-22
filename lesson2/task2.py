# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

original_list = list()

print("Для добавления элемента - введите новое значение и нажмите Enter")
print("Для выхода из режима добавления - оставьте поле ввода пустым и нажмите Enter")

while True:
    item = input("Добавить значение: ")
    if item:
        original_list.append(item)
    else:
        break

replace_list = original_list.copy()

# суть алгоритма - берем четные (по порядку) элементы и меняем местами со следующими элементами
for key in range(0, len(replace_list), 2):
    if key != len(replace_list) - 1:  # не обрабатываем, если дошли до последнего элемента
        replace_list[key], replace_list[key + 1] = replace_list[key + 1], replace_list[key]

print(original_list)
print(replace_list)
