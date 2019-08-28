"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

import random

arr = [random.randint(0, 50) for i in range(random.randint(5,15))]
print(f"Изначальный массив:  {arr}")

def merge_sort(arr):
    if len(arr) > 1:
        center = len(arr) // 2
        left = arr[:center]
        right = arr[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        return arr
    
sortArr = merge_sort(arr) 

print(f"Отсортированный массив:  {sortArr}")
