from finite_element_triangles import Triangle, find_local_s_matrix, find_global_s_matrix
from matrices import Matrix


def q1():
    print('\n=== Question 1 ===')
    S1 = build_triangle_and_find_local_S(
        [0, 0, 0.02],
        [0.02, 0, 0])
    S1.save_to_latex('report/matrices/S1.txt')
    print('S1: {}'.format(S1))

    S2 = build_triangle_and_find_local_S(
        [0.02, 0, 0.02],
        [0.02, 0.02, 0])
    S2.save_to_latex('report/matrices/S2.txt')
    print('S2: {}'.format(S2))

    C = Matrix([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0],
        [0, 0, 1, 0]])
    C.save_to_latex('report/matrices/C.txt')
    print('C: {}'.format(C))

    S = find_global_s_matrix(S1, S2, C)
    S.save_to_latex('report/matrices/S.txt')
    S.save_to_csv('report/csv/S.txt')
    print('S: {}'.format(S))


def build_triangle_and_find_local_S(x, y):
    triangle = Triangle(x, y)
    S = find_local_s_matrix(triangle)
    return S


if __name__ == '__main__':
    q1()
