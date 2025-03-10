# Задание №2
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.

import random as rnd
from typing import Callable

def decor(func: Callable):
    def wrapper(*args, **kwargs):
        a,b,*_ = args
        if a not in range(1,101):
            print(f'Введенное число {a} вне допустимого диапазона. Используем мое число')
            a = rnd.randint(1,100)
        if b not in range (1,11):
            print(f'Введенное число {b} вне допустимого диапазона. Используем мое число')
            b = rnd.randint(1,10)
        return func(a,b)
    return wrapper        
@decor
def inner(a,b):
        print(f'У тебя {b} попыток угадать число ')
        while b:
            guess = int(input('Введите число: '))
            if guess < a:
                print(f'Загаданное число больше чем {guess}')
            elif guess > a:
                print(f'Загаданное число меньше чем {guess}')
            else:
                print(f'Число угаданно! Было загаданно число {a}')
                break
            b -= 1
        else:
            print(f'Попытки закончились, было загаданно число {a}')
    
    
inner(200,5)