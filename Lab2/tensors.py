from math import atan, pi, log, sqrt, radians

import numpy as np


def calculate_hills_tensor(m: np.array, k_0: float, gamma: float) -> np.array:
    ''''''
    axis_tensor = np.array(np.split(np.kron(m, m), 3))
    E = get_unit_tensor()
    f0 = calculate_f0(gamma)

    return (f0 * (E - axis_tensor) + (1 - 2 * f0) * axis_tensor) / k_0

def calculate_dual_hills_tensor(m: np.array, k_0: float, gamma: float) -> np.array:
    P = calculate_hills_tensor(m, k_0, gamma)
    k0 = calculate_conductivity(k_0)
    E = get_unit_tensor()
    print('k0:', k0)
    print('P:', P)
    step_1 = np.tensordot(P, k0, axes=1) #Pc . k_0
    print('dot:', step_1)
    step_2 = E - step_1
    print('step_2:', step_2)
    step_3 = np.tensordot(k0, step_2, axes=1)
    print('step_3: ', step_3)
    return step_3


def calculate_f0(gamma: float) -> float:
    if gamma <= 0.1:
        return pi * gamma / 4
    elif gamma == 1:
        return 1 / 3
    else:
        if gamma > 1:
            g = log((gamma + sqrt(gamma ** 2 - 1)) / (gamma - sqrt(gamma ** 2 - 1))) / 2 / gamma / sqrt(gamma ** 2 - 1)
        elif gamma < 1:
            g = atan(sqrt(1 - gamma ** 2) / gamma) / gamma / sqrt(1 - gamma ** 2)

        return (1 - g) / 2 / (1 - gamma ** (-2))


def get_unit_tensor() -> np.array:
    return np.array(
        [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
    )


def calculate_conductivity(k: float) -> np.array:
    E = get_unit_tensor()

    return k * E

def calculate_axis(x: float, y: float, z: float) -> np.array:
    non_normed = np.array([x, y, z])
    norm = np.linalg.norm(non_normed)

    return non_normed / norm


