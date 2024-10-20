# Напишите программу, находящую такое значение глубины х, при котором
# уровень опасности как можно более близок к нулю. На вход программе
# подаётся максимально допустимое отклонение уровня опасности от нуля, а
# программа должна рассчитать приблизительное значение х, удовлетворяющее
# этому отклонению. Известно, что глубина точно больше нуля и меньше четырёх
# метров. Обеспечьте контроль ввода.


def calculate_danger(x):
    return x**3-3*x**2-12*x+10

def find_safe_depth(user_input):
    d_min = 0
    d_max = 4
    d_middle= (d_min+d_max)/2
    danger_middle = calculate_danger(d_middle)

    while abs(danger_middle) > user_input:
        if danger_middle > 0:
            d_min = d_middle
        else:
            d_max = d_middle
        d_middle= (d_min+d_max)/2
        danger_middle = calculate_danger(d_middle)
    return d_middle

user_input = float(input ("Введите отклонение уровня опасности от нуля: "))
if user_input < 0:
    print('Вы ввели недопустимое значение! Попробуйте еще раз.')
else:
    safe_depth = find_safe_depth(user_input)
    print(f'Приблизительная глубина безопасной кладки: {safe_depth:.9f} м')
