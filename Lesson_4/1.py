"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
Для замеров решил использовать алгоритм из 3го задния 3й домашней работы.

Изначальный код

import random
arr=[]
for i in range(7):
    arr.append(random.randint(2,99))
    
print(f'Изначальный массив:{arr}')

first = arr[0]
second = arr[1]
if first < second:
    maximum = second
    minimum = first
else:
    maximum = first
    minimum = second
    
for a in arr:
    if a > maximum:
        maximum = a
    elif a < minimum:
        minimum = a

def getIndex(arr, num):
    i=0
    for el in arr:
        if arr[i] == num:
            return i
        i+=1
        
a=getIndex(arr, maximum)
b=getIndex(arr, minimum)

arr[a] = minimum
arr[b] = maximum

print(f'Поменяли местами минимальное и максимальное значения:{arr}')

Немного переписываем, чтобы можно было делать замеры через timeit

import random, timeit
arr=[]
for i in range(50):
    arr.append(random.randint(2,999))
    
print(f'Изначальный массив:{arr}')

def findMaxMin(arr):
    first = arr[0]
    second = arr[1]
    if first < second:
        maximum = second
        minimum = first
    else:
        maximum = first
        minimum = second
    
    for a in arr:
        if a > maximum:
            maximum = a
        elif a < minimum:
            minimum = a
    return {'maximum' :maximum,'minimum':minimum}
         
            
dict = findMaxMin(arr)
maximum = dict['maximum']
minimum = dict['minimum']
print(f"Минимальное значение в массиве: {minimum}")
print(f"Максимальное значение в массиве: {maximum}")

def getIndex(arr, num):
    i=0
    for el in arr:
        if arr[i] == num:
            return i
        i+=1
        
a=getIndex(arr, maximum)
b=getIndex(arr, minimum)

arr[a] = minimum
arr[b] = maximum

print(f'Поменяли местами минимальное и максимальное значения:{arr}')

print(timeit.timeit("findMaxMin(arr)", setup="from __main__ import findMaxMin, arr"))
print(timeit.timeit("getIndex(arr, maximum)", setup="from __main__ import getIndex, arr, maximum"))
print(timeit.timeit("getIndex(arr, minimum)", setup="from __main__ import getIndex, arr, minimum"))

по замерам скорость работы с 7ми числами:
1.0342
0.778291563
0.3367191879999998
С 50ю:
4.486068331
1.5939448159999996
1.1912487150000004
Со 100 числами:
7.951808558
9.024859191
8.668280203999998

Переписываем алгоритм со всроенными функциями:
import random, timeit
arr=[]
for i in range(50):
    arr.append(random.randint(2,999))
    
print(f'Изначальный массив:{arr}')

def findMAX(arr):
    return max(arr)
def findMIN(arr):   
    return min(arr)
    
    
maximum =findMAX(arr)
minimum = findMIN(arr)
print(f"Минимальное значение в массиве: {minimum}")
print(f"Максимальное значение в массиве: {maximum}")

def getIndex(arr, num):
    i=0
    for el in arr:
        if arr[i] == num:
            return i
        i+=1
        
a=getIndex(arr, maximum)
b=getIndex(arr, minimum)

arr[a] = minimum
arr[b] = maximum

print(f'Поменяли местами минимальное и максимальное значения:{arr}')

print(timeit.timeit("findMAX(arr)", setup="from __main__ import findMAX, arr"))
print(timeit.timeit("findMIN(arr)", setup="from __main__ import findMIN, arr"))
print(timeit.timeit("getIndex(arr,maximum)", setup="from __main__ import getIndex, arr , maximum"))
print(timeit.timeit("getIndex(arr, minimum)", setup="from __main__ import getIndex, arr, minimum"))

Старый вариант:
по замерам скорость работы с 7ми числами:
1.0342
0.778291563
0.3367191879999998
С 50ю:
4.486068331
1.5939448159999996
1.1912487150000004
Со 100 числами:
7.951808558
9.024859191
8.668280203999998

Новый вариант:
по замерам скорость работы с 7ми числами:
0.425320949
0.43779162999999993
0.7904131759999999
0.5648526370000002
С 50ю:
1.530281636
1.523392334
0.44381258700000004
0.9885496480000002
Со 100 числами:
2.9575999950000003
2.9403687090000004
7.426217405
1.6036813379999995

В обоих вариантах поиск максимального и минимального числа имеет линейную сложность(O(n)).
А перестановка их местами логарифмическую(O(log n)), так сильно зависит от того в где расположены числа.
Позамерам получается, что вариант со встроенными функциями работает незначительно быстрее.
