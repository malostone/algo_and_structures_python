"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

Версия python 3.7 разрядность x64.
Среди сделаных алгоитмов не нашел те у которых прирастает инкримет.
Но рассмотрел несколко примеров.
Первым был рассмотрен алгоритм из первого задания:

import random,math
from memory_profiler import profile
from pympler import asizeof


min = int(input("Введите минимальную границу случайного числа: "))
max = int(input("Введите максимальную границу случайного числа: "))

@profile
def check_int(min,max): 
    if min > max:
        return "Минимальное число больше максимального"
    else:
        number = math.floor(random.random() * (max - min)) + min
        return f"Случайное целое число {number}"
@profile   
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

@profile
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
print(asizeof.asizeof(min_letter))
print(asizeof.asizeof(max_letter))
print(asizeof.asizeof(min))

Питон выдал такие данные:

Line #    Mem usage    Increment   Line Contents
================================================
     9     16.4 MiB     16.4 MiB   @profile
    10                             def check_int(min,max):
    11     16.4 MiB      0.0 MiB       if min > max:
    12                                     return "Минимальное число больше максимального"
    13                                 else:
    14     16.4 MiB      0.0 MiB           number = math.floor(random.random() * (max - min)) + min
    15     16.4 MiB      0.0 MiB           return f"Случайное целое число {number}"


Случайное целое число 102
Filename: hw4.py

Line #    Mem usage    Increment   Line Contents
================================================
    16     16.4 MiB     16.4 MiB   @profile
    17                             def check_float(min,max):
    18     16.4 MiB      0.0 MiB       if min > max:
    19                                     return "Минимальное число больше максимального"
    20                                 else:
    21     16.4 MiB      0.0 MiB           number = random.random() * (max - min) + min
    22     16.4 MiB      0.0 MiB           return f"Случайное вещественное  число {number}"


Случайное вещественное  число 76.77891472829619
Введите любой символ английского алфавита: a
Введите любой символ английского алфавита: z
Filename: hw4.py

Line #    Mem usage    Increment   Line Contents
================================================
    30     16.4 MiB     16.4 MiB   @profile
    31                             def check_letter(min,max):
    32     16.4 MiB      0.0 MiB       max = ord(max)
    33     16.4 MiB      0.0 MiB       min = ord(min)
    34     16.4 MiB      0.0 MiB       if min > max:
    35                                     return "Расположите буквы в алфавитном порядке"
    36                                 else:
    37     16.4 MiB      0.0 MiB           number = math.floor(random.random() * (max - min)) + min
    38     16.4 MiB      0.0 MiB           symbol = chr(number)
    39     16.4 MiB      0.0 MiB           return f"Случайный символ {symbol}"


Случайный символ k
56
56
32

Инкрементов нет, при изменении границ числа размер переменной не менялся, хоть 1 хоть 9999.

Второй алгоритм был 3е задание из 3й домашней работы.

import random
from memory_profiler import profile
from pympler import asizeof

arr=[]
for i in range(100):
    arr.append(random.uniform(2,99))
    
#print(f'Изначальный массив:{arr}')

@profile
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

@profile
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

#print(f'Поменяли местами минимальное и максимальное значения:{arr}')

print(asizeof.asizeof(arr))
print(asizeof.asizeof(maximum))
print(asizeof.asizeof(minimum))

Результаты

Line #    Mem usage    Increment   Line Contents
================================================
    10     16.3 MiB     16.3 MiB   @profile
    11                             def findMAX(arr):
    12     16.3 MiB      0.0 MiB       return max(arr)


Filename: hw3.1.py

Line #    Mem usage    Increment   Line Contents
================================================
    13     16.3 MiB     16.3 MiB   @profile
    14                             def findMIN(arr):
    15     16.3 MiB      0.0 MiB       return min(arr)


Минимальное значение в массиве: 4
Максимальное значение в массиве: 99
Filename: hw3.1.py

Line #    Mem usage    Increment   Line Contents
================================================
    23     16.3 MiB     16.3 MiB   @profile
    24                             def getIndex(arr, num):
    25     16.3 MiB      0.0 MiB       i=0
    26     16.3 MiB      0.0 MiB       for el in arr:
    27     16.3 MiB      0.0 MiB           if arr[i] == num:
    28     16.3 MiB      0.0 MiB               return i
    29     16.3 MiB      0.0 MiB           i+=1


Filename: hw3.1.py

Line #    Mem usage    Increment   Line Contents
================================================
    23     16.3 MiB     16.3 MiB   @profile
    24                             def getIndex(arr, num):
    25     16.3 MiB      0.0 MiB       i=0
    26     16.3 MiB      0.0 MiB       for el in arr:
    27     16.3 MiB      0.0 MiB           if arr[i] == num:
    28     16.3 MiB      0.0 MiB               return i
    29     16.3 MiB      0.0 MiB           i+=1

3088
32
32

Инкриментов также, но изменяя границы случайного числа вес переменнойпостоянно менялся.
При границах 2,99 он составли 3088.
Но если сдвинуть границы 2,9999 то вес вырастает до 4112.
А если снизить до 2,9 то вес кардинально снижается до 1168.
Вероятнее это связано, с тем что все хранится в двоичном виде.

Также если использовать алгоритм со встроенной функцией поискак максимумам или минимума:

import random
from memory_profiler import profile
from pympler import asizeof

arr=[]
for i in range(100):
    arr.append(random.randint(2,9))
    
print(f'Изначальный массив:{arr}')
@profile
def findMAX(arr):
    return max(arr)
@profile
def findMIN(arr):   
    return min(arr)
    
    
maximum =findMAX(arr)
minimum = findMIN(arr)
print(f"Минимальное значение в массиве: {minimum}")
print(f"Максимальное значение в массиве: {maximum}")

@profile
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

print(asizeof.asizeof(arr))
print(asizeof.asizeof(maximum))
print(asizeof.asizeof(minimum))

То вес алгоритма вырастает на 0,1:
Filename: hw3.1.py

Line #    Mem usage    Increment   Line Contents
================================================
    23     16.4 MiB     16.4 MiB   @profile
    24                             def getIndex(arr, num):
    25     16.4 MiB      0.0 MiB       i=0
    26     16.4 MiB      0.0 MiB       for el in arr:
    27     16.4 MiB      0.0 MiB           if arr[i] == num:
    28     16.4 MiB      0.0 MiB               return i
    29     16.4 MiB      0.0 MiB           i+=1




