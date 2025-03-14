# Задание №1
# Погружение в Python | Функции
# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.

def funk_1(str):
    list_1 = str.lower().split()
    list_1.sort()
    max_len=len(max(list_1, key=len))
    for i, item in enumerate(list_1, 1):
        print(f'{i}. {item:>{max_len+1}}')

data='Слова выводятся отсортированными согласно кодировки Unicode.'
funk_1(data)