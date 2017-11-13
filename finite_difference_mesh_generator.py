from matrices import Matrix


def generate_finite_diff_mesh(mesh_size, num_free_nodes):
    """
    Generates a finite-difference mesh with the given size and number of free nodes.

    :param mesh_size: the mesh size
    :param num_free_nodes: the number of free nodes
    :return: the A and b matrices defining the mesh equation (Ax = b)
    """
    A = Matrix.empty(num_free_nodes, num_free_nodes)
    b = Matrix.empty(num_free_nodes, 1)
    for row in range(mesh_size - 3):
        for col in range(mesh_size - 1):
            node = row * (mesh_size - 1) + col
            A[node][node] = -4

            if row != 0:
                A[node][node - mesh_size + 1] = 1
            if 12 <= node <= 14:
                b[node][0] = -15
            else:
                A[node][node + mesh_size - 1] = 1

            # Right Neumann boundary
            if col == mesh_size - 2:
                A[node][node - 1] = 2
            else:
                if col != 0:
                    A[node][node - 1] = 1
                A[node][node + 1] = 1

    # Special nodes
    A[15][10] = 1
    A[15][15] = -4
    A[15][16] = 1
    A[15][17] = 1

    A[16][11] = 1
    A[16][15] = 1
    A[16][16] = -4
    A[16][18] = 1
    b[16][0] = -15

    A[17][15] = 2
    A[17][17] = -4
    A[17][18] = 1

    A[18][16] = 2
    A[18][17] = 1
    A[18][18] = -4
    b[18][0] = -15

    return A, b
