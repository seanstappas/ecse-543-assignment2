from __future__ import division

from matrices import Matrix


class Triangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = (x[1] * y[2] - x[2] * y[1] - x[0] * y[2] + x[2] * y[0] + x[0] * y[1] - x[1] * y[0]) / 2


def find_local_S_matrix(triangle):
    x = triangle.x
    y = triangle.y
    S = Matrix.empty(3, 3)

    for i in range(3):
        for j in range(3):
            S[i][j] = ((y[(i + 1) % 3] - y[(i + 2) % 3]) * (y[(j + 1) % 3] - y[(j + 2) % 3])
                       + (x[(i + 1) % 3] - x[(i + 2) % 3]) * (x[(j + 1) % 3] - x[(j + 2) % 3])) / (4 * triangle.area)

    return S
