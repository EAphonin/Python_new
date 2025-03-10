# Задание №5
# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.
from task3 import decor as json_decor
from task2 import decor as param_control_decor
from task4 import outer as counter

@json_decor
@counter(2)
@param_control_decor
def guess_number(a,b):
        print(f'У тебя {b} попыток угадать число ')
        while b:
            guess = int(input('Введите число: '))
            if guess < a:
                print(f'Загаданное число больше чем {guess}')
            elif guess > a:
                print(f'Загаданное число меньше чем {guess}')
            else:
                print(f'Число угаданно! Было загаданно число {a}')
                return f'ты угадал за {b} попыток. Было загаданно число {a}'
            b -= 1
        else:
            print(f'Попытки закончились, было загаданно число {a}')
            return f'не угадал было загаданно число {a}'

guess_number(123, 3)