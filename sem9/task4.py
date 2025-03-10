# Задание №4
# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.

from typing import Callable

def outer(count: int):

    def decor(func: Callable):
        res =[]
        def wrapper(*args, **kwargs):
            for _ in range(count):
                res.append(func(*args, **kwargs))
            return res

        return wrapper
    return decor

@outer(10)
def some_func(a: str, b:str):
    return a + '_' + b

print(some_func('1', '2'))