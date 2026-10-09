# -*- coding: cp1251 -*-
from math import tan


def f2t(x, x1, y1, x2, y2):
    '''Задание линейной функции по двум точкам '''
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    return k * x + b


def f(x):
    '''Прошлая функуия'''
    if -5 <= x <= -2:
        return f2t(x, -5, -1, -2, 0)
    elif -2 < x <= 2:
        return tan(x / 2)
    elif -2 < x <= 5:
        return f2t(x, 3, 0, 5, 1)


while True:
    try:
        output = ""
        print("Функция определена на отрезке [-5, 5]")
        Xbeg = float(input("Введите Xbeg="))
        Xend = float(input("Введите Xend="))
        dx = float(input("Введите dx="))
        if dx == 0: raise ValueError

        output += '\n'
        output += f"{"X":^8} | {"Y":^8}\n"
        output += '\n'

        Xt = Xbeg
        while Xt < Xend:
            output += f"{Xt:^8.2f} | {f(Xt):^8.2f}\n"
            Xt += dx

        print(output)
        with open("03_1.txt", "w", encoding="utf-8") as f:
            f.write(output)
            print("Данный записаны в файл 03_1.txt")
        break
    except:
        print("Ошибка! Попробуйте ещё раз!")
        continue
