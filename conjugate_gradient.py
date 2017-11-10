from matrices import Matrix


def conjugate_gradient(A, b):
    n = len(A)
    x = Matrix.empty(1, n)
    r = b - A * x
    p = r
    for _ in range(n):
        denom = p.tranpose() * A * p
        alpha = p.tranpose() * r / denom
        x = x + alpha * p
        r = b - A * x
        beta = - p.transpose() * A * r / denom
        p = r + beta * p
    return x
