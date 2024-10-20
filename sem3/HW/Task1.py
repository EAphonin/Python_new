# Дан список повторяющихся элементов. Вернуть список с дублирующимися
# элементами. В результирующем списке не должно быть дубликатов

import random


list_1 = [random.randint(1,10) for _ in range (10)]
print(list_1)
result = []

for i in list_1:
    if list_1.count(i) >= 1 and i not in result:
        result.append(i)
print(result)

