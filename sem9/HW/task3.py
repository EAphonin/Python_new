# Задача 3. Счётчик
# Реализуйте декоратор counter, считающий и выводящий количество вызовов
# декорируемой функции.
# Для решения задачи нельзя использовать операторы global и nonlocal.

from functools import wraps
from typing import Callable, Optional

def counter(func: Callable) -> Callable:
    @wraps
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        result = func(*args, **kwargs)
        print(f"Функцию {func.__name__} вызвали {wrapper.count} раз")
        return result
    wrapper.count = 0
    return wrapper

@counter
def greeting(name: str, age: Optional[int] = None) -> str:
    
    if age:
        return "Огоб {name}! Тебе уже {age} лет, ты очень старый".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)
    
def main():
    greeting("Vasya")
    greeting("Musya", age = 15)

main()