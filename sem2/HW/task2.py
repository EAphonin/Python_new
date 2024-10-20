# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
# Для проверки своего кода используйте модуль fractions.
from fractions import Fraction


frac1 = '1/2'
frac2 = '1/3'

numerator1 = int(frac1.split('/')[0])
denominator1 = int(frac1.split('/')[1])

numerator2 = int(frac2.split('/')[0])
denominator2 = int(frac2.split('/')[1])

denominator_general = denominator1*denominator2
sum = numerator1*denominator2+numerator2*denominator1
proiz = numerator1*numerator2

print(f'Сумма дробей: {sum} / {denominator_general}')
print(f'Произведение дробей: {proiz} / {denominator_general}')
sum2=Fraction(frac1)+Fraction(frac2)
proiz2=Fraction(frac1)*Fraction(frac2)
print(sum2)
print(proiz2)