#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

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
