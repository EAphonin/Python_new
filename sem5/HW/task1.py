# Задание 1. Квадраты чисел
# Пользователь вводит число N. Напишите программу, которая генерирует
# последовательность из квадратов чисел от 1 до N (1 ** 2, 2 ** 2, 3 ** 2 и так
# далее). Реализацию напишите двумя способами: функция-генератор и
# генераторное выражение.

def generator_function(n: int):
    for i in range(1, n+1):
        yield i**2

print(*generator_function(3))    

n = 4
generator_expr = (i ** 2 for i in range(1, n + 1))
for square in generator_expr:
    print(square, end=' ')
