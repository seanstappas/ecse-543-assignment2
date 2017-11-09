from __future__ import division

from matrices import Matrix


class Triangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = (x[1] * y[2] - x[2] * y[1] - x[0] * y[2] + x[2] * y[0] + x[0] * y[1] - x[1] * y[0]) / 2


def find_local_s_matrix(triangle):
    x = triangle.x
    y = triangle.y
    S = Matrix.empty(3, 3)

    for i in range(3):
        for j in range(3):
            S[i][j] = ((y[(i + 1) % 3] - y[(i + 2) % 3]) * (y[(j + 1) % 3] - y[(j + 2) % 3])
                       + (x[(i + 1) % 3] - x[(i + 2) % 3]) * (x[(j + 1) % 3] - x[(j + 2) % 3])) / (4 * triangle.area)

    return S


def find_global_s_matrix(S1, S2, C):
    S_dis = find_disjoint_s_matrix(S1, S2)
    S_dis.save_to_latex('report/matrices/S_dis.txt')
    print('S_dis: {}'.format(S_dis))
    return C.transpose() * S_dis * C


def find_disjoint_s_matrix(S1, S2):
    n = len(S1)
    S_dis = Matrix.empty(2 * n, 2 * n)
    for row in range(n):
        for col in range(n):
            S_dis[row][col] = S1[row][col]
            S_dis[row + n][col + n] = S2[row][col]
    return S_dis
