# Задача 2. Модуль для удаления дублирующихся подряд символов
# Напишите модуль с функцией, которая принимает строку и возвращает строку с
# удаленными дублирующимися подряд идущими символами. Например, строка
# "aabbccaa" должна быть преобразована в "abca".

def del_double(str1: str) -> str:
    if not str1:
        return str1
    list1=list(str1[0])
    for char in str1[1:]:
        if char != list1[-1]:
            list1.append(char)
    return ''.join(list1)