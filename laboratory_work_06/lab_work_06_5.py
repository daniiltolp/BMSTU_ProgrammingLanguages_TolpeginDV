# -*- coding: cp1251 -*-
# Вариант 23
import numpy as np


def create_matrix(size, low=-10, high=10):
    """Инициализация матрицы случайными целыми числами."""
    return np.random.randint(low, high + 1, size=(size, size))


def write_matrix(matr, title, fo):
    """Запись матрицы в выходной файл через f-строки."""
    fo.write(f"{title}\n")
    rows, cols = matr.shape
    for i in range(rows):
        for j in range(cols):
            fo.write(f"{matr[i, j]:5d} ")
        fo.write("\n")
    fo.write("\n")


def calculate_block_sums(matr, n, fo):
    """Вычисление и запись сумм элементов блоков матрицы в файл."""
    # Разбиение матрицы на блоки размером n x n
    b1 = matr[0:n, 0:n]  # Левый верхний
    b2 = matr[0:n, n:2 * n]  # Правый верхний
    b3 = matr[n:2 * n, 0:n]  # Левый нижний
    b4 = matr[n:2 * n, n:2 * n]  # Правый нижний

    sums = []
    for b_idx, block in enumerate([b1, b2, b3, b4], start=1):
        total = 0
        for i in range(n):
            for j in range(n):
                total += block[i, j]
        sums.append(total)
        fo.write(f"Сумма элементов блока {b_idx}: {total}\n")
    fo.write("\n")
    return sums


def rearrange_blocks(matr, n):
    """Циклическая перестановка блоков матрицы."""
    new_matr = np.zeros((2 * n, 2 * n), dtype=int)

    for i in range(n):
        for j in range(n):
            new_matr[i, j] = matr[n + i, j]
            new_matr[i, n + j] = matr[i, j]
            new_matr[n + i, j] = matr[n + i, n + j]
            new_matr[n + i, n + j] = matr[i, n + j]
    return new_matr


def main():
    n = int(input("Введите параметр n (размер матрицы будет 2n x 2n): "))
    size = 2 * n

    tst_matr = create_matrix(size)

    fh_i = open("lab_work_06_5_in.txt", "wb")
    np.savetxt(fh_i, tst_matr, fmt="%5d")
    fh_i.close()

    fh_i = open("lab_work_06_5_in.txt", "rt")
    matrix = np.loadtxt(fh_i, dtype=int, ndmin=2)
    fh_i.close()

    rows, cols = matrix.shape
    n_matr = rows // 2

    result_matrix = rearrange_blocks(matrix, n_matr)

    fo = open("lab_work_06_5_out.txt", "wt", encoding="cp1251")

    write_matrix(matrix, f"Исходная матрица ({rows}x{cols}):", fo)
    fo.write("--- Суммы блоков ---\n")
    calculate_block_sums(matrix, n_matr, fo)
    write_matrix(result_matrix, "После перестановки блоков:", fo)

    fo.close()
    print("Матрица сгенерирована в lab_work_06_5_in.txt, результат записан в lab_work_06_5_out.txt")


if __name__ == "__main__":
    main()
