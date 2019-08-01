# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

if second < first < third or third < first < second:
    print('Среднее число:', first)
elif first < second < third or third < second < first:
    print('Среднее число:', second)
else:
    print('Среднее число:', third)
