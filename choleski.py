from __future__ import division

import math

from matrices import Matrix


def choleski_solve(A, b, half_bandwidth=None):
    """
    Solves an Ax = b matrix equation by Choleski decomposition.
    :param A: the A matrix
    :param b: the b matrix
    :param half_bandwidth: the half-bandwidth of the A matrix
    :return: the solved x vector
    """
    n = len(A[0])
    if half_bandwidth is None:
        elimination(A, b)
    else:
        elimination_banded(A, b, half_bandwidth)
    x = Matrix.empty(n, 1)
    back_substitution(A, x, b)
    return x


def elimination(A, b):
    """
    Performs the elimination step of Choleski decomposition.
    :param A: the A matrix
    :param b: the b matrix
    """
    n = len(A)
    for j in range(n):
        if A[j][j] <= 0:
            raise ValueError('Matrix A is not positive definite.')
        A[j][j] = math.sqrt(A[j][j])
        b[j][0] = b[j][0] / A[j][j]
        for i in range(j + 1, n):
            A[i][j] = A[i][j] / A[j][j]
            b[i][0] = b[i][0] - A[i][j] * b[j][0]
            for k in range(j + 1, i + 1):
                A[i][k] = A[i][k] - A[i][j] * A[k][j]


def elimination_banded(A, b, half_bandwidth):
    """
    Performs the banded elimination step of Choleski decomposition.
    :param A: the A matrix
    :param b: the b matrix
    :param half_bandwidth: the half_bandwidth to be used for the banded elimination
    """
    n = len(A)
    for j in range(n):
        if A[j][j] <= 0:
            raise ValueError('Matrix A is not positive definite.')
        A[j][j] = math.sqrt(A[j][j])
        b[j][0] = b[j][0] / A[j][j]
        max_row = min(j + half_bandwidth, n)
        for i in range(j + 1, max_row):
            A[i][j] = A[i][j] / A[j][j]
            b[i][0] = b[i][0] - A[i][j] * b[j][0]
            for k in range(j + 1, i + 1):
                A[i][k] = A[i][k] - A[i][j] * A[k][j]


def back_substitution(L, x, y):
    """
    Performs the back-substitution step of Choleski decomposition.
    :param L: the L matrix
    :param x: the x matrix
    :param y: the y matrix
    """
    n = len(L)
    for i in range(n - 1, -1, -1):
        prev_sum = 0
        for j in range(i + 1, n):
            prev_sum += L[j][i] * x[j][0]
        x[i][0] = (y[i][0] - prev_sum) / L[i][i]