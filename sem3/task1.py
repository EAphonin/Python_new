# Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка. 
import random


list_1 = [1, 2, 3, 4, 6, 7, 8, 6, 4, 3]
new_list = []
for i in list_1:
    if i not in new_list:
        new_list.append(i)
print(new_list)

print(nums := [random.randint(0,10) for _ in range(20)])
print(list(set(nums)))