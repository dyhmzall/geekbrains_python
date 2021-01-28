# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = 0

while (month < 1) or (month > 12):
    try:
        month = int(input("Введите месяц в виде целого числа (от 1 до 12): "))
    except Exception as e:
        print("Ошибка! Программа не смогла распознать введенное вами число")
        pass

# вариант решения задачи через List
season_names = ['зима', 'весна', 'лето', 'осень']
season_months = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]

for index, months in enumerate(season_months):
    if month in months:
        print(f"Ваш месяц относится к сезону {season_names[index]}")
        break

# вариант решения задачи через dict
seasons = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}

for season, months in seasons.items():
    if month in months:
        print(f"Ваш месяц относится к сезону {season}")
        break
