# Задание №3
# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.
# def funk_1(str):
#     list_1=str.split()
#     for i in range(len(list_1)):
#         list_1[i]= int(list_1[i])
#     list_1.sort()
#     dict_1 = {chr(i): i for i in range(list_1[0], list_1[1]+1)}
#     return dict_1
# str_input= input('Введите два числа через пробел: ')
# print(funk_1(str_input))

def dict_unicode(some_str: str) -> dict:
    lims = sorted([int(i) for i in some_str.split()])
    return {chr(i): i for i in range(lims[0], lims[1]+1)}

print(dict_unicode('1123 1145'))