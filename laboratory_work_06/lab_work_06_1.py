# Вариант 23

def f1(a, c):
    part1 = (1 + 6 * a * c) / (a ** 3 - 8 * c ** 3) - 1 / (a - 2 * c)
    part2 = 1 / (a ** 3 - 8 * c ** 3) - 1 / (a ** 2 + 2 * a * c + 4 * c ** 2)
    return part1 / part2


def f2(a, c):
    return 1 - 2 * c + a


fi = open("lab_work_06_1_in.txt", "rt")
fo = open("lab_work_06_1_out.txt", "wt")

fi.readline()
fi.readline()

fo.write(f"{'a':>8} {'c':>8} {'z1':>10} {'z2':>10}\n")

for line in fi:
    if line == "\n" or not line.strip():
        continue
    b, d = line.split()
    a = float(b)
    c = float(d)
    try:
        z1 = f1(a, c)
        z2 = f2(a, c)
    except:
        print(f'Недопустимые значения в строке {line}')
        continue
    fo.write(f"{a:8.2f} {c:8.2f} {z1:10.4f} {z2:10.4f}\n")

fi.close()
fo.close()
