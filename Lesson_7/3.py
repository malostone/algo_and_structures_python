"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""

import random

def getMedian(orig_list):
    for i in range(len(orig_list)):
        m = 0
        n = 0
        for j in range(len(orig_list)):
            if orig_list[j] != orig_list[i]:
                if orig_list[j] > orig_list[i]:
                    n += 1
                else:
                    m += 1
        if n == m:
            return orig_list[i]

randNumb = random.randint(1, 100)
orig_list = [random.randint(1, 100) for _ in range(2*randNumb+1)]

print(orig_list)
a = getMedian(orig_list)
print(a)
