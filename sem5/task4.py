# Задание №4
# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.

print(
    *(x for x in range(0,101,2) if sum(list(map(int, str(x)))) !=8)
)
