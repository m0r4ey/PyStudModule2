# Функции в Python. Функция с параметром.

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix = []
        for j in range(m):
            if i == j:
                matrix.append(1)
            else:
                matrix.append(value)
        print(matrix)
    return matrix

# Немного усложнил выводом по диагонали единиц
matrix = get_matrix(10, 10, 0)