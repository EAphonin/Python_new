# Напишите программу, которая генерирует случайный пароль заданной длины,
# состоящий из букв, цифр и специальных символов

import random
import string


len = int(input("Введите длину пароля: "))
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(chars) for i in range(len))
print(password)
