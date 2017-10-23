from finite_element import Triangle, find_local_S_matrix


def q1():
    build_triangle_and_find_local_S(
        [0, 0, 0.02],
        [0.02, 0, 0])
    build_triangle_and_find_local_S(
        [0.02, 0, 0.02],
        [0.02, 0.02, 0])


def build_triangle_and_find_local_S(x, y):
    triangle = Triangle(x, y)
    S = find_local_S_matrix(triangle)
    print('S matrix: {}'.format(S))


if __name__ == '__main__':
    q1()
