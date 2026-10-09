from math import sin, cos, sqrt, atan2, pi


def f(x, y, r):
    in_circle = (x ** 2 + y ** 2) <= r ** 2
    obl1 = (0 <= x <= r) and (-r <= y <= 0) and in_circle
    obl2 = (-r <= x <= 0) and (0 <= y <= r) and not in_circle
    return obl1 or obl2


x = float(input("Введите X="))
y = float(input("Введите Y="))
R = float(input("Введите R="))

print(f"Точка {x:.2f}, {y:.2f} {"" if f(x, y, R) else "не"} попадает в область.")
