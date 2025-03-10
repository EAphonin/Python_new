# Задание 1. Как дела?
# Вася совсем заскучал на работе и решил побаловаться с кодом проекта. Он
# написал надоедливый декоратор, который при вызове декорируемой функции
# спрашивает у пользователя «Как дела?», вне зависимости от ответа пишет что-то
# вроде «А у меня не очень!» и только потом запускает саму функцию. Правда, после
# такой выходки Васю чуть не уволили с работы.
# Реализуйте такой же декоратор и проверьте его работу на нескольких функциях.

from functools import wraps
from typing import Callable, Any

def how_are_you (func: Callable) -> Callable:
    @wraps
    def wrapper(*args, **kwargs):
        input('How are you?')
        print('А у меня не очень. На свою функцию')
        result = func(*args, **kwargs)
        return result
    
    return wrapper
@how_are_you
def test1():
    print('Test #1')

result=test1()