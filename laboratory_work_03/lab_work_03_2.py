from random import uniform


def f(x, y, r):
    in_circle = (x ** 2 + y ** 2) <= r ** 2
    obl1 = (0 <= x <= r) and (-r <= y <= 0) and in_circle
    obl2 = (-r <= x <= 0) and (0 <= y <= r) and not in_circle
    return obl1 or obl2


R = float(input("Введите R="))
print(f"{"X":^5} | {"Y":^5} | {"res":^5}")
for i in range(10):
    x, y = uniform(-1, 4), uniform(-1, 10)
    flag = f(x, y, R)
    print(f"{x:^5.2f} | {y:^5.2f} |  ", end="")
    print(f"{"Yes" if flag else "No"}")
