"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random

def bubble_sort(orig_list):
    n = len(orig_list)-1
    while n > 0:
        i = len(orig_list)-1
        swap = False
        while i > len(orig_list)-n-1:
            if orig_list[i] < orig_list[i-1]:
                orig_list[i],orig_list[i-1] = orig_list[i-1],orig_list[i]
                swap = True
            i-=1
        n -= 1
        if swap == False:
            break
    return orig_list


orig_list = [random.randint(-100, 100) for _ in range(100)]

print(orig_list)
a = bubble_sort(orig_list)
print(a)
