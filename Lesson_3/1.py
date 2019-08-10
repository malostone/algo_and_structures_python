# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

dict = {i: 0 for i in range (2,10)}
for i in range (2,100):
    for a in  dict:
        if i % a == 0:
            dict[a] = dict[a] + 1
for a in dict:
    print(f'Количство кратных {a} равно {dict[a]}')
