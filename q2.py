INNER_CONDUCTOR_POINTS = [28, 29, 30, 34]
OUTER_CONDUCTOR_POINTS = [1, 2, 3, 4, 5, 6, 7, 13, 19, 25, 31]

MESH_SIZE = 6

def q2():
    with open('simple2d/mesh.dat', 'w') as f:
        generate_node_positions(f)
        generate_triangle_coordinates(f)
        generate_initial_potentials(f)


def generate_node_positions(f):
    for row in range(MESH_SIZE):
        y = row * 0.02
        for col in range(MESH_SIZE):
            x = col * 0.02
            node = row * MESH_SIZE + (col + 1)
            if node <= 34:  # Inner conductor
                f.write('{} {} {}\n'.format(node, x, y))
    f.write('\n')


def generate_triangle_coordinates(f):
    # Left triangles
    for row in range(MESH_SIZE - 1):
        for col in range(MESH_SIZE - 1):
            node = row * MESH_SIZE + (col + 1)
            if node < 28:
                f.write('{} {} {} 0\n'.format(node, node + 1, node + MESH_SIZE))

    # Right triangles
    for row in range(MESH_SIZE - 1):
        for col in range(1, MESH_SIZE):
            node = row * MESH_SIZE + (col + 1)
            if node <= 28:
                f.write('{} {} {} 0\n'.format(node, node + MESH_SIZE - 1, node + MESH_SIZE))

    f.write('\n')


def generate_initial_potentials(f):
    for point in OUTER_CONDUCTOR_POINTS:
        f.write('{} {}\n'.format(point, 0))
    for point in INNER_CONDUCTOR_POINTS:
        f.write('{} {}\n'.format(point, 15))


if __name__ == '__main__':
    q2()
