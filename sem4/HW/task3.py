# Задача 3. Число наоборот
# Пользователь вводит два числа: N и K. Напишите программу, которая заменяет
# каждое число на число, которое получается из исходного записью его цифр в
# обратном порядке, затем складывает их, снова переворачивает и выводит
# ответ на экран.
# Пример:
# Введите первое число: 102
# Введите второе число: 123
# Первое число наоборот: 201
# Второе число наоборот: 321
# Сумма: 522
# Сумма наоборот: 225

user_num1 = int(input('Введите первое число: '))
user_num2 = int(input('Введите второе число: '))

def revers(num):
    count = 0
    result = 0
    for _ in str(num):
        count+=1
    while num>0:
        count-=1
        result +=num%10*(10**count)
        num//=10
    return result

def summ(num1,num2):
    sum_num = num1+ num2
    return sum_num

result1= revers(user_num1)
result2= revers(user_num2)
summ_num=summ(result1,result2)
print(result1,result2,summ_num)