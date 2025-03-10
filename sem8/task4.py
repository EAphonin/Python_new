# Задание №4
# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.

def export_csv_to_json(csv_file:str, json_file:str):
    with open(csv_file, 'r', encoding='utf-8') as file:
        data = file.readlines()
    for i, items in enumerate(data):
        data[i] = data[i].strip
        print(data)

export_csv_to_json("user.csv", 'new_users.json')