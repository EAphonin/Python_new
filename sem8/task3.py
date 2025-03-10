# Задание №3
# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

import csv
import json

def json_to_csv(json_filename='users.json', csv_filename='user.csv'):
    try:
        with open(json_filename, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        with open (csv_filename, 'w', encoding='utf-8', newline='') as csv_file:
            writer = csv.writer(csv_file)

            writer.writerow(['Access level', 'User ID', 'Name'])

            for access_level, users in data.items():
                for user_id, name in users.items():
                    writer.writerow([access_level, user_id, name])
        print(f"Данные успешно загружены в {csv_filename}")
    except FileNotFoundError:
        print(f"Ошибка: файл {json_filename} не найден")

json_to_csv()