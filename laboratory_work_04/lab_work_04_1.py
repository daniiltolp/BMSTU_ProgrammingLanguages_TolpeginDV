# вариант 23
from random import uniform

n = int(input("Элементов в массиве: (N<=30) "))
if n > 30: n = 30
if n < 5: n = 5

s = [uniform(-5, 5) for i in range(n)]
print("Начальное состояние: ", [f"{i:.2f}" for i in s])

# второй по величине элемент
mx2 = (float("-inf"), 0)
mx1 = (float("-inf"), 0)
for i in range(len(s)):
    if s[i] > mx1[0]:
        mx2 = mx1
        mx1 = (s[i], i)
    elif s[i] > mx2[0]:
        mx2 = (s[i], i)
print(f"Максимальный: {mx1[0]:.2f} (индекс {mx1[1]})")
print(f"Второй по величине: {mx2[0]:.2f} (индекс {mx2[1]})")

# сумма элементов между максимальным и вторым по величине
sm = sum(s[min(mx1[1], mx2[1]) + 1:max(mx1[1], mx2[1])])
print(f"Сумма элементов между ними: {sm:.2f}")

# упорядочить по возрастанию остаткос от их делания на второй по величине элемент
s_sorted = sorted(s, key=lambda x: (x % mx2[0]))
print("Отсортированный массив: ", [f"{i:.2f}" for i in s_sorted])
print(f"Остатки от деления на {mx2[0]:.2f}:  ", [f"{(i % mx2[0]):.2f}" for i in s_sorted])
