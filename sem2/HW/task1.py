# Напишите программу, которая получает целое число num и 
# возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def to_hex(num):
    hex_digits = '0123456789abcdef'
    hex_str = ''
    while num:
        hex_str = hex_digits[num%16]+hex_str
        num //= 16
    return hex_str.upper()

num = 255
hex_str = to_hex(num)
print(f'Шестнадцатеричное представление числа: {hex_str}')
print(f'Проверка результата: {hex(num)}')