from __future__ import division

from matrices import Matrix


class Triangle:
    """Represents a finite-difference triangle."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = (x[1] * y[2] - x[2] * y[1] - x[0] * y[2] + x[2] * y[0] + x[0] * y[1] - x[1] * y[0]) / 2


def find_local_s_matrix(triangle):
    """
    Finds the local S matrix for a finite-difference triangle.

    :param triangle: the finite-difference triangle
    :return: the local S matrix
    """
    x = triangle.x
    y = triangle.y
    S = Matrix.empty(3, 3)

    for i in range(3):
        for j in range(3):
            S[i][j] = ((y[(i + 1) % 3] - y[(i + 2) % 3]) * (y[(j + 1) % 3] - y[(j + 2) % 3])
                       + (x[(i + 1) % 3] - x[(i + 2) % 3]) * (x[(j + 1) % 3] - x[(j + 2) % 3])) / (4 * triangle.area)

    return S


def find_global_s_matrix(S1, S2, C):
    """
    Finds the global S matrix given by two local S matrices and the the connectivity matrix.

    :param S1: the first local S matrix
    :param S2: the second local S matrix
    :param C: the connectivity matrix
    :return: the global S matrix
    """
    S_dis = find_disjoint_s_matrix(S1, S2)
    S_dis.save_to_latex('report/matrices/S_dis.txt')
    print('S_dis: {}'.format(S_dis))
    return C.transpose() * S_dis * C


def find_disjoint_s_matrix(S1, S2):
    """
    Finds the disjoint S matrix given by the two provided local S matrices.

    :param S1: the first local S matrix
    :param S2: the second local S matrix
    :return: the disjoint S matrix
    """
    n = len(S1)
    S_dis = Matrix.empty(2 * n, 2 * n)
    for row in range(n):
        for col in range(n):
            S_dis[row][col] = S1[row][col]
            S_dis[row + n][col + n] = S2[row][col]
    return S_dis
