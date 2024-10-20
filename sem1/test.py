# a=2;  b=2; c=2
# if a+b>c and a+c>b and b+c>a:
#     print('Треугольник существует')
#     if a == b and a == c:
#         print('Треугольник равносторонний')
#     elif a ==b or a ==c:
#         print('Треугольник равнобедренный')
#     else: 
#         print('Треугольник разносторонний')
    
# else:
#     print('Треугольник не существует')
    
# num = int(input('Введите число'))
# k = 0
# if num >100000 or num< 1:
#     print('Число должно быть больше 1 и меньше 100000')
    
# else: 
#     for i in range(2, num// 2+1):
#         if (num%i == 0):
#             k=k+1
#     if (k == 0):
#         print('Число простое')
#     else:
#         print('Число составное')

list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

count = 0
for i in list1:
    for j in list2:
        if i == j:
            count+=1
print('Количество совпадающих чисел: ',count)