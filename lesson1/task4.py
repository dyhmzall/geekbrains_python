# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

num = int(input("Введите целое положительное число: "))

# начальная цифра
digit = 0

while num:
    if num % 10 > digit:
        digit = num % 10
    num //= 10

print(f"Самая болшая цифра в числе: {digit}")