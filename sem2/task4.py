# Задание №4
# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

from decimal import Decimal
import decimal
import math
decimal.getcontext().prec = 42
d = Decimal(input('Введите диаметр: '))
s = Decimal(math.pi) * pow((d/2), 2)
c = Decimal(math.pi)*d

print(f' S = {s} , C = {c}')