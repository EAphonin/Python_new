# Напишите программу, которая принимает список чисел через строку и
# возвращает наибольшее число в этом списке.
str_1 = input("Введите числа через пробел: ")
list_1 = [int(x) for x in str_1.split()]
print(list_1)
print(max(list_1))

max_num2=list_1[0]
for i in range(len(list_1)):
    if max_num2 < list_1[i]:
        max_num2 = list_1[i]
print(max_num2)