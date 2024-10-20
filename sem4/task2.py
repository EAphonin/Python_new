# Задание №2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.
def funk_1(str):
    str = set(str)
    list_1=[]
    for i in str:
        list_1.append(ord(i))
    list_1.sort(reverse=True)
    return list_1

data="808998998"
print(funk_1(data))

print([ord(i) for i in sorted(list(set(data)), reverse= True)])