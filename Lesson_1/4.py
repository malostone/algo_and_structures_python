"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""

import random,math

min = int(input("Введите минимальную границу случайного числа: "))
max = int(input("Введите максимальную границу случайного числа: "))

def check_int(min,max): 
    if min > max:
        return "Минимальное число больше максимального"
    else:
        number = math.floor(random.random() * (max - min)) + min
        return f"Случайное целое число {number}"
    
def check_float(min,max): 
    if min > max:
        return "Минимальное число больше максимального"
    else:
        number = random.random() * (max - min) + min
        return f"Случайное вещественное  число {number}"
    
print(check_int(min,max))
print(check_float(min,max))

min_letter = input("Введите любой символ английского алфавита: ")
max_letter = input("Введите любой символ английского алфавита: ")

def check_letter(min,max):
    max = ord(max)
    min = ord(min)
    if min > max:
        return "Расположите буквы в алфавитном порядке"
    else:
        number = math.floor(random.random() * (max - min)) + min
        symbol = chr(number)
        return f"Случайный символ {symbol}"
    
print(check_letter(min_letter,max_letter))
