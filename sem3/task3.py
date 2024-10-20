# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

import random


list_1 = [random.randint(0,10) for _ in range (20)]
print(list_1)
i = 0
while i <len(list_1):
    item = list_1[i]
    if list_1.count(item) >= 2:        
            list_1.remove(item)
            list_1.remove(item)
    else:
          i+=1
print(list_1)        