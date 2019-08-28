"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

import hashlib

s = input("Введите строку из маленьких латинских букв: ")
result = set()

N = len(s)


for i in range(N):
    if i == 0:
        N = len(s) - 1
    else:
        N = len(s)
    for j in range(N, i, -1):
        print(s[i:j])
        result.add(hashlib.md5(s[i:j].encode('utf-8')).hexdigest())
print(result)


print(f'Количество различных подстрок в строке {s} равно {len(result)}')
