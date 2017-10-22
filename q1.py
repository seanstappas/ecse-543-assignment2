from finite_element import Triangle, find_local_S_matrix


def q1():
    x = [0, 0, 0.02]
    y = [0.02, 0, 0]
    triangle = Triangle(x, y)
    S = find_local_S_matrix(triangle)
    print('S matrix: {}'.format(S))


if __name__ == '__main__':
    q1()
