from copy import deepcopy

from matrices import Matrix


def conjugate_gradient_solve(A, b, residual_vectors=None):
    """
    Solves the Ax = b matrix equation given by the given A and b matrices

    :param A: the A matrix
    :param b: the b matrix
    :param residual_vectors: the list to store the residual vectors in
    :return: the solved x vector
    """
    n = len(A)
    x = Matrix.empty(n, 1)
    r = b - A * x
    p = deepcopy(r)
    if residual_vectors is not None:
        residual_vectors.append(r)
    for _ in range(n):
        denom = p.transpose() * A * p
        alpha = (p.transpose() * r) / denom
        x = x + p * alpha.item()
        r = b - A * x
        beta = - (p.transpose() * A * r) / denom
        p = r + p * beta.item()
        if residual_vectors is not None:
            residual_vectors.append(r)
    return x
