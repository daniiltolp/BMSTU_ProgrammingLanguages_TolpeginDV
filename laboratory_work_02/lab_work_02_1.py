# -*- coding: cp1251 -*-
# вариант 23
from math import tan


def f2(x, x1, y1, x2, y2):
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    return k * x + b


x = float(input('Введите значение x='))

if -5 <= x <= -2:
    y = f2(x, -5, -1, -2, 0)
elif -2 < x <= 2:
    y = tan(x / 2)
elif 2 < x <= 5:
    y = f2(x, 3, 0, 5, 1)
print(f"X={x:.2f}        Y={y:.2f}")
