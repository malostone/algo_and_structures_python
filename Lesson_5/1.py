"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

import random
from collections import namedtuple

quantity = int(input("Введите кол-во предприятий"))

Enterprise = namedtuple('Enterprise' , 'name income')

enterprises = []

for i in range(quantity):
    enterprise = Enterprise(
        name = input(f"Введите название предприятия {i + 1}"),
        income = [random.randint(0,100000) for i in range(4)])
    enterprises.append(enterprise)

arr = []
for item in enterprises:
    arr = arr + item.income

def getAverage(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return sum/len(arr)

average = getAverage(arr)

for item in enterprises:
    if getAverage(item.income) > average:
        print(f"Прибыль предприятия {item.name} выше среднего")
    elif getAverage(item.income) < average:
        print(f"Прибыль предприятия {item.name} ниже среднего")
