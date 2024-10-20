# Напишите программу, которая принимает два слова и определяет, являются ли
# они анаграммами.
word_1 = input("Введите первое слово: ")
word_2 = input("Введите второе слово: ")

if len(word_1) != len(word_2) :
    print("Слова не являются аннограмми")
else:
    char_word_1 = {}
    char_word_2 = {}
    for char in word_1:
        if char in char_word_1:
            char_word_1[char] += 1
        else:
            char_word_1[char] = 1
    for char in word_2:
        if char in char_word_2:
            char_word_2[char] += 1
        else:
            char_word_2[char] = 1
    if char_word_1 == char_word_2:
        print("Слова являются аннограмми")
    else:
        print("Слова не являются аннограмми")