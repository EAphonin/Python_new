# Задача 2. Замедление кода
# В программировании иногда возникает ситуация, когда работу функции нужно
# замедлить. Типичный пример — функция, которая постоянно проверяет,
# изменились ли данные на веб-странице или её код.
# Реализуйте декоратор, который перед выполнением декорируемой функции
# ждёт несколько секунд.

from functools import wraps
from time import sleep
from typing import Callable

def slowdown_2s(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        sleep(2)
        result = func(*args, **kwargs)
        return result
    return wrapper

@slowdown_2s
def test():
    print('test')
@slowdown_2s
def test2():
    print('test2')
test()
test2()