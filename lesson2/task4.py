# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

user_string = input("Введите строку из нескольки строк: ")

for index, string in enumerate(user_string.split(), 1):
    print(index, string[:10])
