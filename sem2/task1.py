# a=2
# b= 4.6
# c='string'

# print(type(a))
# print(type(b))
# print(type(c))

data = [1,4.5, 'str', 2,4.5, True, False]

for i in range(len(data)):
    print(f'порядковый номер: {i+1}')
    print(f'значение: {data[i]}')
    print(f'Адрес в памяти: {id(data[i])}')
    print(f'размер: {data[i].__sizeof__()}')
    print(f'хэш: {hash(data[i])}')
    if isinstance(data[i], int| float):
        print('Это число')
    if isinstance(data[i], str):
        print('Это строка')
    print('\n' + '='*20 + '\n')