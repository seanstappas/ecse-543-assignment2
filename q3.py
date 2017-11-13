from finite_difference_mesh_generator import generate_finite_diff_mesh

MESH_SIZE = 6


def q3():
    print('\n=== Question 3 ===')
    q3a()


def q3a():
    print('\n=== Question 3(a) ===')
    A, b = generate_finite_diff_mesh(MESH_SIZE, 19)
    print('A: {}'.format(A.integer_string()))
    print('b: {}'.format(b.integer_string()))
    print('A is positive definite: {}'.format(A.is_positive_definite()))
    A_prime = A.transpose() * A
    print("A' is positive definite: {}".format(A_prime.is_positive_definite()))


if __name__ == '__main__':
    q3()
