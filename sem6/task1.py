from random import randint

def my_func (min_num = 0, max_num = 100, count = 10):
    number = randint(min_num, max_num+1)
    while count:
        num = int(input(f'Введите число от {min_num} до {max_num}: '))
        if(min_num <= num <=max_num):
            if num == number:
                print("Вы угадали число. ")
                break
            elif  num < number:
                print("Ваше число меньше загадоного ")
            else: 
                print("Ваше число больше заданного")
        else: 
            print("Введено число не из диапазона")
            break
        count -= 1
    print(number)

