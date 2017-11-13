from copy import deepcopy

import matplotlib.pyplot as plt

from matplotlib import rc
from matplotlib.ticker import MaxNLocator

from choleski import choleski_solve
from conjugate_gradient import conjugate_gradient_solve
from finite_difference_mesh_generator import generate_finite_diff_mesh

MESH_SIZE = 6
NUM_FREE_NODES = 19
rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)


def q3():
    print('\n=== Question 3 ===')
    A, b = q3a()
    choleski_potential, cg_potential, residual_vectors = q3b(A, b)
    q3c(residual_vectors)
    q3d(choleski_potential, cg_potential)


def q3a():
    print('\n=== Question 3(a) ===')
    A, b = generate_finite_diff_mesh(MESH_SIZE, NUM_FREE_NODES)
    print('A: {}'.format(A.integer_string()))
    print('b: {}'.format(b.integer_string()))
    print('A is positive definite: {}'.format(A.is_positive_definite()))
    A_prime = A.transpose() * A
    b_prime = A.transpose() * b
    print("A' is positive definite: {}".format(A_prime.is_positive_definite()))
    return A_prime, b_prime


def q3b(A, b):
    print('\n=== Question 3(b) ===')
    A_copy = deepcopy(A)
    b_copy = deepcopy(b)
    x_choleski = choleski_solve(A_copy, b_copy)
    print('Choleski x: {}'.format(x_choleski))
    residual_vectors = []
    x_cg = conjugate_gradient_solve(A, b, residual_vectors)
    print('Conjugate gradient x: {}'.format(x_cg))
    node_6_4 = 7
    return x_choleski[node_6_4][0], x_cg[node_6_4][0], residual_vectors


def q3c(residual_vectors):
    print('\n=== Question 3(c) ===')
    plot_residual_norms(residual_vectors, infinity_norm=False)
    plot_residual_norms(residual_vectors, infinity_norm=True)


def q3d(choleski_potential, cg_potential):
    print('\n=== Question 3(d) ===')
    print('Choleski potential at (0.06, 0.04): {} V'.format(choleski_potential))
    print('Conjugate gradient potential at (0.06, 0.04): {} V'.format(cg_potential))


def plot_residual_norms(residual_vectors, infinity_norm=False):
    f = plt.figure()
    ax = f.gca()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    x_range = [i for i in range(len(residual_vectors))]
    y_range = [v.infinity_norm() if infinity_norm else v.two_norm() for v in residual_vectors]
    plt.plot(x_range, y_range, 'o-{}'.format('C0' if infinity_norm else 'C1'),
             label=''.format('Infinity norm' if infinity_norm else '2-norm'))
    plt.xlabel('Conjugate gradient iteration ($k$)')
    plt.ylabel('Infinity norm of residual vector $(\\|\\textbf{r}\\|_\\infty)$' if infinity_norm
               else '2-norm of residual vector $(\\|\\textbf{r}\\|_2)$')
    plt.grid(True)
    f.savefig('report/plots/q3c_{}.pdf'.format('infinity' if infinity_norm else '2'), bbox_inches='tight')


if __name__ == '__main__':
    q3()
