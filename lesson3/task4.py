# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
    """Возвещение x в степень y (простой вариант)"""
    return x ** y


def my_func2(x, y):
    """Возвещение x в степень y (сложный вариант)"""
    result = 1
    for i in range(abs(y)):
        result *= x
    return 1 / result


error_message = "Ошибка! Попробуйте еще раз!"

while True:
    try:
        x = float(input("Введите действительное положительное число х: "))
        if x < 0:
            print(error_message)
            continue
        break
    except ValueError:
        print(error_message)
        continue

while True:
    try:
        y = int(input("Введите целое отрицательное число y: "))
        if y >= 0:
            print(error_message)
            continue
        break
    except ValueError:
        print(error_message)
        continue

print(my_func(x, y))
print(my_func2(x, y))
