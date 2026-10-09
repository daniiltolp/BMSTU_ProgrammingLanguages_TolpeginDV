# вариант 23
from random import uniform

# Чтение количества элементов из входного файла
with open("lab_work_06_4_in.txt", "r", encoding="cp1251") as fi:
    n = int(fi.readline().strip())

if n > 30: n = 30
if n < 5: n = 5

s = [uniform(-5, 5) for i in range(n)]

# второй по величине элемент
mx2 = (float("-inf"), 0)
mx1 = (float("-inf"), 0)
for i in range(len(s)):
    if s[i] > mx1[0]:
        mx2 = mx1
        mx1 = (s[i], i)
    elif s[i] > mx2[0]:
        mx2 = (s[i], i)

# сумма элементов между максимальным и вторым по величине
sm = sum(s[min(mx1[1], mx2[1]) + 1:max(mx1[1], mx2[1])])

# упорядочить по возрастанию остатков от их деления на второй по величине элемент
s_sorted = sorted(s, key=lambda x: (x % mx2[0]))

# Запись всех результатов в выходной файл
with open("lab_work_06_4_out.txt", "w", encoding="cp1251") as fo:
    fo.write(f"Начальное состояние: {[f'{i:.2f}' for i in s]}\n")
    fo.write(f"Максимальный: {mx1[0]:.2f} (индекс {mx1[1]})\n")
    fo.write(f"Второй по величине: {mx2[0]:.2f} (индекс {mx2[1]})\n")
    fo.write(f"Сумма элементов между ними: {sm:.2f}\n")
    fo.write(f"Отсортированный массив: {[f'{i:.2f}' for i in s_sorted]}\n")
    fo.write(f"Остатки от деления на {mx2[0]:.2f}: {[f'{(i % mx2[0]):.2f}' for i in s_sorted]}\n")
