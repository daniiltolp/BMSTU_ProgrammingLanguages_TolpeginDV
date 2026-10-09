from math import log

print("Введите Xbeg, Xend, Dx и Eps")
xb = float(input("Xbeg = "))
xe = float(input("Xend = "))
dx = float(input("Dx = "))
eps = float(input("Eps = "))

print("     X         Y      Y_exact    N    ")

xt = xb
while xt <= xe:
    # Проверка области допустимых значений: (2x + 1)^2 > 1
    if (2 * xt + 1) ** 2 <= 1:
        print(f" {xt:8.2f}    Ряд расходится (нужно x > 0 или x < -1)   ")
    else:
        n = 0
        an = 2.0 / (2 * xt + 1)
        y = an

        while True:
            k = (2 * n + 1) / ((2 * n + 3) * ((2 * xt + 1) ** 2))
            an = an * k
            y += an
            n += 1
            if abs(an) < eps:
                break

        y_exact = log((xt + 1) / xt)
        print(f" {xt:8.2f}  {y:8.4f}  {y_exact:8.4f}  {n + 1:5}  ")
    xt += dx
