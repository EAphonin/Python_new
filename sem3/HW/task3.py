# Напишите программу, которая принимает строку и определяет, является ли она
# палиндромом (читается одинаково с обеих сторон).
str_1 = ("а роза упала на лапу Азора").lower().replace(' ','')
print(str_1[::-1])
if str_1 == str_1[::-1]:
    print(f"{str_1} - Это полиндром")
else:
    print(f"{str_1} - Это НЕ полиндром")

result = set()
for ch in str_1:
    if ch in result:
        result.remove(ch)
    else:
        result.add(ch)

if len(result) <=1:
    print(f"{str_1} - Это полиндром")
else:
    print(f"{str_1} - Это НЕ полиндром")