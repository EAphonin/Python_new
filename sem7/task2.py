# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

from random import randint, sample, uniform
import string

NUM_OF_NAMES = randint (3, 10)
vowels = 'aeiouy'
def write_in_file():
    names = []
    while len(names) < NUM_OF_NAMES:
        res = ''.join(sample(string.ascii_lowercase, randint(4,7))).title()
        if len(set(res) & set(vowels)) > 0:
            names.append(res)
    with open(f'Sem7_02.txt', 'a', encoding='utf-8') as f:
        f.writelines('\n'.join(names))

write_in_file()