from matrices import Matrix

E_0 = 8.854187817620E-12


def extract_mesh():
    with open('simple2d/result.dat') as f:
        mesh = {}
        for line_number, line in enumerate(f):
            if line_number >= 2:
                vals = line.split()
                node = int(float(vals[0]))
                voltage = float(vals[3])
                mesh[node] = voltage
    return mesh


def compute_half_energy(S, mesh, mesh_size):
    U_con = Matrix.empty(4, 1)
    half_energy = 0
    for row in range(mesh_size - 1):
        for col in range(mesh_size - 1):
            node = row * mesh_size + (col + 1)  # 1-based
            if node < 28:
                U_con[0][0] = mesh[node + mesh_size]
                U_con[1][0] = mesh[node]
                U_con[2][0] = mesh[node + 1]
                U_con[3][0] = mesh[node + mesh_size + 1]
                half_energy_contribution = U_con.transpose() * S * U_con
                half_energy += half_energy_contribution[0][0]
    return half_energy


def find_capacitance(S, voltage, mesh_size):
    mesh = extract_mesh()
    half_energy = compute_half_energy(S, mesh, mesh_size)
    capacitance = (4 * E_0 * half_energy) / voltage ** 2
    return capacitance
