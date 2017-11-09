from finite_element_capacitance import find_capacitance
from matrices import Matrix
from finite_element_mesh_generator import generate_simple_2d_mesh

INNER_CONDUCTOR_POINTS = [28, 29, 30, 34]
OUTER_CONDUCTOR_POINTS = [1, 2, 3, 4, 5, 6, 7, 13, 19, 25, 31]

MESH_SIZE = 6


def q2():
    print('\n=== Question 2 ===')
    q2a()
    q2c()


def q2a():
    generate_simple_2d_mesh(MESH_SIZE, INNER_CONDUCTOR_POINTS, OUTER_CONDUCTOR_POINTS)


def q2c():
    print('\n=== Question 2(c) ===')
    S = Matrix.csv_to_matrix('report/csv/S.txt')
    voltage = 15
    capacitance = find_capacitance(S, voltage, MESH_SIZE)
    print('Capacitance per unit length: {} F/m'.format(capacitance))


if __name__ == '__main__':
    q2()
