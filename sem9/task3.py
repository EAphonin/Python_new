# Задание №3
# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.

from typing import Callable
import json
import os

def decor(func: Callable) -> Callable:
    
    def wrapper(*args, **kwargs):
        file_name = func.__name__ + '.json'
    
        if os.path.isfile(file_name) and os.path.exists(file_name):
            with open(file_name, 'r', encoding='UTF-8') as file:
                data = json.load(file)
        else:
            data = dict()    

        result = func(*args, **kwargs)
        data[result] = list(args + tuple(kwargs.items()))
        with open(file_name, 'w', encoding='UTF-8') as file:
            data= json.dump (data, file, indent= 4, ensure_ascii=False)
        return result
    return wrapper

@decor
def some_func(a: str, b:str):
    return a + '_' + b

some_func('1', '2')
some_func(b = '13', a = '2s')
some_func('3', b= 'sadf2')
