# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

import math

number = int(input("Введите трехзначное число :"))

first = math.floor(number / 100)
second = math.floor((number / 10) % 10)
third = math.floor(number % 10)

summ = first + second + third
multiplication = first * second * third

print(f"Сумма чисел: {summ} ")
print(f"Произведение чисел: {multiplication}")
