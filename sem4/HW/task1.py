# Задание 1. Апгрейд калькулятора
# Степан использует калькулятор для расчёта суммы и разности чисел, но на
# работе ему требуются не только обычные арифметические действия. Он ничего
# не хочет делать вручную, поэтому решил немного расширить функционал
# калькулятора.
# Напишите программу, запрашивающую у пользователя число и действие,
# которое нужно сделать с числом: вывести сумму его цифр, максимальную или
# минимальную цифру. Каждое действие оформите в виде отдельной функции, а
# основную программу зациклите.
# Запрошенные числа должны передаваться в функции суммы, максимума и
# минимума при помощи аргументов.



def digits_sum (num):
    summ = 0
    while num > 0:
        digit = num%10
        summ += digit
        num //=10
    print(f'Сумма чисел {user_num} = {summ}')

def maximum(num):
    max_num = 0
    while num > 0:
        digit = num%10
        if digit > max_num:
            max_num = digit
        num //= 10
    print(f'Максимальная цифра числа {user_num} - {max_num}')

def minimum(num):
    min_num = num%10
    while num > 0:
        digit = num%10
        if digit < min_num:
            min_num = digit
        num //= 10
    print(f'Минимальная цифра числа {user_num} - {min_num}')

while True:
    user_num = int(input('Введите число: '))
    action = int(input('Введите номер действия: 1 - сумма цифр, 2 - max цифра, 3 - min цифра: '))
    if action == 1:
        digits_sum(user_num)
    elif action == 2:
        maximum(user_num)
    elif action == 3:
        minimum(user_num)
    else:
        print("Неверная команда.")