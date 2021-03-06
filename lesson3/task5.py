# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def sum_number_in_string(string):
    """
    Вытащить из строки числа и просуммировать их
    :param string: str
    :return: float, bool
    """
    summa = 0
    for number in string.split():

        if number == 'q':
            return summa, True

        # не число просто пропускаем
        try:
            summa += float(number)
        except ValueError:
            continue

    return summa, False


summa = 0
is_end = False

while True:
    string = input("Введите числа через пробел или символ 'q' для завершения: ")
    current_summa, is_end = sum_number_in_string(string)
    summa += current_summa

    print(f"Общая сумма составляет {summa}")

    if is_end:
        break

print("Программа завершена!")
