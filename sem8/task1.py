# Задание №1
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json

def convert_to_json(input_file, output_file):
    data = {}

    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            key, value = line.strip().split(' ')
            key = key.capitalize()
            data[key]=value

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

convert_to_json('Sem7_03.txt', 'result.json')