# Задание №2
# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку. 

str1= "Самостоятельно сохраните в переменной строку текста"

my_dict = {i: ord(i) for i in str1}
print(my_dict)