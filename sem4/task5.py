# Задание №5
# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии. 

def get_dict(names, stv, prem):
    return {names[i]: stv[i]*float(prem[i][:-1])/100 for i in range(len(names))}

print(get_dict(["Иван", "Андрей"], [1000,2000], ["12%", "15.5%"]))