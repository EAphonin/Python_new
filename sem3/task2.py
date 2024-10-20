# Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

from pprint import pp
tuple_1 = (1, 2, 3, "1", '2', True, False, [1,2,3,4])
result = dict()

for i in tuple_1:
    if type(i) not in result:
        result[type(i)] = []
    result[type(i)].append(i)

pp(result)