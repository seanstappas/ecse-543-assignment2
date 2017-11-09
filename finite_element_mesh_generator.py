
def generate_simple_2d_mesh(mesh_size, inner_conductor_points, outer_conductor_points):
    with open('simple2d/mesh.dat', 'w') as f:
        generate_node_positions(f, mesh_size)
        generate_triangle_coordinates(f, mesh_size)
        generate_initial_potentials(f, inner_conductor_points, outer_conductor_points)


def generate_node_positions(f, mesh_size):
    for row in range(mesh_size):
        y = row * 0.02
        for col in range(mesh_size):
            x = col * 0.02
            node = row * mesh_size + (col + 1)
            if node <= 34:  # Inner conductor
                f.write('{} {} {}\n'.format(node, x, y))
    f.write('\n')


def generate_triangle_coordinates(f, mesh_size):
    # Left triangles (left halves of squares)
    for row in range(mesh_size - 1):
        for col in range(mesh_size - 1):
            node = row * mesh_size + (col + 1)
            if node < 28:
                f.write('{} {} {} 0\n'.format(node, node + 1, node + mesh_size))

    # Right triangles (right halves of squares)
    for row in range(mesh_size - 1):
        for col in range(1, mesh_size):
            node = row * mesh_size + (col + 1)
            if node <= 28:
                f.write('{} {} {} 0\n'.format(node, node + mesh_size - 1, node + mesh_size))

    f.write('\n')


def generate_initial_potentials(f, inner_conductor_points, outer_conductor_points):
    for point in outer_conductor_points:
        f.write('{} {}\n'.format(point, 0))
    for point in inner_conductor_points:
        f.write('{} {}\n'.format(point, 15))
