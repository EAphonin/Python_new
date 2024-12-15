import sys
from task4 import correct_date 
# if len(sys.argv) != 2:
#     print("Usage: python date_validator.py DD.MM.YYYY")
#     sys.exit(1)

date_input = input("Введите дату ")
print(date_input)
print(correct_date(date_input))