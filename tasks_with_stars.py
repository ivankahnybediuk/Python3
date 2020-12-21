import random

# """
# Задание (із зірочкой):
# Получить от пользователя его номер телефона, проверить подходит ли номер под форматы
# +380_________ (прочерки - любая цифра)
# 0_________ (например 0931233232)
# 0__ ___ __ __ (пробелы именно пробелы и телефон например 095 321 12 21)
# Если номер введен верно - похвалите человека. Если нет - поругайте.
# """
phone_number = input('Please enter your phone number  ')
if phone_number[:4].strip() == '+380' and phone_number[4:].strip().isdigit() and len(phone_number.strip()) == 13:
    print('Thank you for entering valid phone number!')

else:
    print('Please, enter right phone number!')

# """
# Задание 2 пример по математике просто решить глядя в код, а что если переменную инициализировать случайным значением?
# В первой строке импортируйте модуль рандома
# import random
# обьявите переменные (случайное целое от 1 до 20 включительно)
# var1 = random.randint(1,20)
# Теперь сделайте задание 2 но уже со случайными значениями.
# """
number1 = random.randint(1, 20)
number2 = random.randint(1, 20)
result = input(f'{number1} + {number2} = ' )
if int(result) == number1+number2:
    print('Yes! You`re right!')
else:
    print('No! It`s incorect!')
# """
# Задание 3
# проверить что введенная строка является полиндромом.
# """
word = input ("Write some word ")
if word == word[::-1]:
    print('Yes! Its palindrome')
else:
    print('No! It isn`t palindrome!')