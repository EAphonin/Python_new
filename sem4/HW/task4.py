# Помогите Юре написать программу, которая находит максимум из трёх чисел.
# Для этого используйте только функцию нахождения максимума из двух чисел.
# По итогу в программе должны быть реализованы две функции:
# 1. maximum_of_two — функция принимает два числа и возвращает одно
# (наибольшее из двух);
# 2. maximum_of_three — функция принимает три числа и возвращает одно
# (наибольшее из трёх); при этом она должна использовать для сравнений
# первую функцию maximum_of_two.

user_num1 = int(input('Введите первое число: '))
user_num2 = int(input('Введите второе число: '))
user_num3 = int(input('Введите третье число: '))

def maximum_of_two(a,b):
    if a > b:
        return a
    else:
        return b

def maximum_of_three(c):
    temp = maximum_of_two(user_num1, user_num2)
    if temp > c:
        return temp
    else:
        return c

max_numb = maximum_of_three(user_num3)

print(f'Из чисел {user_num1}, {user_num2}, {user_num3} максимальное {max_numb}')