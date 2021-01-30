# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(number1, number2):
    """Возвращает деление первого параметра на второе"""
    try:
        result = number1 / number2
    except ZeroDivisionError:
        result = None
    return result


def number_input(message):
    """Обеспечивает ввод корректного значения"""
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print("Ошибка! Нужно ввести именно число!")
            continue


number1 = number_input("Введите делимое: ")
number2 = number_input("Введите чстное: ")

result = division(number1, number2)

if result is None:
    print("Делить на 0 нельзя!")
else:
    print(f"Результат деления {number1:.2f} на {number2:.2f} равен {result:.2f}")