import numpy as np


def create_matrix(size, low=-10, high=10):
    """Инициализация матрицы случайными целыми числами"""
    return np.random.randint(low, high + 1, size=(size, size))


def print_matrix(matr, title=''):
    """вывод матрицы на экран."""
    print(title)
    rows, cols = matr.shape
    for i in range(rows):
        for j in range(cols):
            print(f"{matr[i, j]:5d}", end=" ")
        print()
    print()


def calculate_block_sums(matr, n):
    """Вычисление и вывод суммы элементов каждого из  блоков."""
    # Разбиение матрицы на блоки размером n x n
    b1 = matr[0:n, 0:n]  # Левый верхний
    b2 = matr[0:n, n:2 * n]  # Правый верхний
    b3 = matr[n:2 * n, 0:n]  # Левый нижний
    b4 = matr[n:2 * n, n:2 * n]  # Правый нижний

    # Вычисление сумм
    sums = []
    for b_idx, block in enumerate([b1, b2, b3, b4], start=1):
        total = 0
        for i in range(n):
            for j in range(n):
                total += block[i, j]
        sums.append(total)
        print(f"Сумма элементов блока {b_idx}: {total}")
    print()
    return sums


def rearrange_blocks(matr, n):
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

    matrix = create_matrix(size)
    print_matrix(matrix, f"Исходная матрица ({size}x{size}):")

    print("--- Суммы элементов блоков исходной матрицы ---")
    calculate_block_sums(matrix, n)

    result_matrix = rearrange_blocks(matrix, n)

    print_matrix(result_matrix, f"Матрица после циклической перестановки блоков:")


if __name__ == "__main__":
    main()
