# Задание №4
# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

def my_sort(some_list: list):
    for i in range(1, len(some_list)):
        for j in range(len(some_list)-i):
            if some_list[j] > some_list[j+1]:
                some_list[j],some_list[j+1] = some_list[j+1], some_list[j]

lst = [1,2,5,79,2,1,4,3,0]
my_sort(lst)
print(lst)