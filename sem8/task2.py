# Задание №2
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.

import json
import os

def add_users_to_json(filename = 'users.json'):
   
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load (file)
    else:
        data = {str(level): {} for level in range(1,8)}
    
    while True:
        name = input("Введите имя пользователя (или 'exit' для выхода): ")
        if name.lower() == 'exit':
            break
        
        user_id = input("Введите личный идентификатор пользователя: ")
        access_level = input("Введите уровень доступа (от 1 до 7): ")

        if any(user_id in users for users in data.values()):
            print("Ошибка: Идентификатор должен быть уникальным.")
            continue
        if access_level not in data:
            print("Ошибка: Уровень доступа должен быть от 1 до 7.")
            continue
        data[access_level][user_id] = name

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent = 2, ensure_ascii = False)

        print("Пользователь успешно добавлен!")

add_users_to_json()