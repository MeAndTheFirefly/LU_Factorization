import numpy as np
from numpy.linalg import inv

#matrix = np.array([[1, 1, 1, 5], [2, 3, 5, 8], [4, 0, 5, 2]], dtype=float)
#matrix = np.array([[1, 2, -3, 2], [6, 3, -9, 6], [7, 14, -21, 13]], dtype=float)
#matrix = np.array([[2, 6, -2, 3], [4, 8, -5, 4], [0, 4, 1, 2]], dtype=float)
matrix = np.array([[2, -2, 3], [6, -7, 14], [4, -8, 30]], dtype=float)


def elementary_matrix(m):
    res = []
    i_matrix = np.identity(len(m))  # obtain identity matrix
    j = 0
    for i in range(len(m) - 1):
        j = i
        while j < len(m) - 1:
            temp = i_matrix.copy()  # can't assign directly, otherwise share the same reference
            temp[j+1][i] = - m[j+1][i] / m[i][i]  # elementary matrix
            res.append(temp)
            m = np.matmul(temp, m)  # multiply elementary matrix with original one
            j += 1
    return res


def inverse_elementary_matrix(list_elem):   # inverse of each elementary matrix
    res_inverse = []
    for mat in list_elem:
        res_inverse.append(inv(mat))
    return res_inverse


def upper_triangular_matrix(m):
    res = elementary_matrix(m)
    for i in range(len(res)):
        m = np.matmul(res[i], m)
    return m


def lower_triangular_matrix(m):
    res = inverse_elementary_matrix(elementary_matrix(m))
    mat = res[0]
    for i in range(len(res) - 1):
        mat = np.matmul(mat, res[i + 1])
    return mat


print(lower_triangular_matrix(matrix))




