# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


def generate_random_name():
    def generate_random_word(word):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(random.randint(1, 15)):
            word += (random.choice(letters))
        return word

    while True:
        word_1 = generate_random_word('')
        word_2 = generate_random_word('')
        yield f"{word_1} {word_2}"


# Здесь пишем код
gen = generate_random_name()
print(next(gen))
