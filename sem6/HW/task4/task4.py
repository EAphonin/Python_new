# Задача 4. Модуль для проверки даты
# Создайте модуль и напишите в нём функцию, которая получает на вход дату в
# формате DD.MM.YYYY Функция возвращает истину, если дата может существовать
# или ложь, если такая дата невозможна. Для простоты договоримся, что год
# может быть в диапазоне [1, 9999]. Весь период (1 января 1 года - 31 декабря 9999
# года) действует Григорианский календарь. Проверку года на високосность
# вынести в отдельную защищённую функцию.

def correct_date(date: str) -> bool:
    if len(date) != 10:
        return False
    
    date_parts = date.split('.')
    if date_parts != 3:
        return False
    try:
        day, month, year = map(int,date_parts)
    except ValueError:
        return False
    if not (1<=month<=12):
        return False
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2:
        if is_leap_year(year) and day > 29:
            return False
        elif not is_leap_year(year) and day > 28:
            return False
    return True
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)