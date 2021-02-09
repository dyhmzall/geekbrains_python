"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

# Запускать скрипт нужно по формату (порядок не имеет значение)
# $ python task1.py hours=10 rate=2500 prize=5000

from sys import argv, exit


def calc_zp(hours, rate, prize):
    return (hours * rate) + prize


params = {}

for param in argv:
    if param.find('=') > 0:  # пропускаем параметры не по формату
        key, value = param.split('=')
        params[key] = float(value)

for param_name in ['hours', 'rate', 'prize']:
    if param_name not in params:
        print("Должны быть заполнены все параметры, например hours=10 rate=2500 prize=5000")
        exit(1)  # выход из программы

print(f"Зарплата составляет: {calc_zp(**params)}")
