# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.
str_1 = " ser de lur from Austrelia" 
list_1 = str_1.split()
len_max = max(list_1, key = len)
len_max = len(len_max)+1
list_1.sort()
for num, value in enumerate(list_1, 1):
    print(f"{num}.{value:>{len_max}}")
    