# Задание №3
# ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

# a = int(input('Введите число'))
# a2 = a

# bin_num = ''
# oct_num = ''
# while a:
#     if a%2 == 0:
#         bin_num = '0' + bin_num
#     else:
#         bin_num = '1' + bin_num
#     a //=2
# print(bin_num)
# print(bin(a2))

num = int(input('Введите число: '))
base = int(input('Введите систему счисления: '))

original_num = num
result_num = ''

while num:
    result_num = str(num%base) + result_num 
    num //= base

print(f'Число {original_num} в {base}-ичной системе счисления равно {result_num}')
print(bin(original_num)[2:] if base == 2 else oct(original_num)[2:])