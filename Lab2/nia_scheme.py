from typing import List, Annotated

import numpy as np
from tensors import calculate_conductivity, calculate_hills_tensor, calculate_axis, calculate_dual_hills_tensor

def calculate_effective_conductivity(p_1: float, type_inh: int, k_0: float, k_1: float, m: Annotated[List[float], 3], gamma: float) -> np.array:
    if len(m) != 3:
        raise ValueError('Должен быть передан список из трех чисел.')
    volume_fraction_map = {
        1: [p_1 / 2, p_1 / 2],
        2: [p_1, 0],
        3: [0, p_1]
    }
    p_sph, p_sphd = volume_fraction_map.get(type_inh)
    p_0 = 1 - (p_sph + p_sphd)
    k0 = calculate_conductivity(k_0)
    k1 = calculate_conductivity(k_1)
    m = calculate_axis(*m)
    P_sph = calculate_hills_tensor(m, k_0, 1)
    P_sphd = calculate_hills_tensor(m, k_0, gamma)

    del_k = np.linalg.inv(k1 - k0) if k_1 != k_0 else None

    if del_k.any():
        return k0 + p_sph * np.linalg.inv(del_k + P_sph) + p_sphd * np.linalg.inv(del_k + P_sphd)
    else:
        return k0

def calculate_effective_conductivity_dual(p_1: float, type_inh: int, k_0: float, k_1: float, m: Annotated[List[float], 3], gamma: float) -> np.array:
    if len(m) != 3:
        raise ValueError('Должен быть передан список из трех чисел.')
    volume_fraction_map = {
        1: [p_1 / 2, p_1 / 2],
        2: [p_1, 0],
        3: [0, p_1]
    }
    p_sph, p_sphd = volume_fraction_map.get(type_inh)
    p_0 = 1 - (p_sph + p_sphd)
    r0 = calculate_conductivity(k_0 ** (-1))
    r1 = calculate_conductivity(k_1 ** (-1))
    m = calculate_axis(*m)
    Q_sph = calculate_dual_hills_tensor(m, k_0, 1)
    Q_sphd = calculate_dual_hills_tensor(m, k_0, gamma)

    del_r = np.linalg.inv(r1 - r0) if k_1 != k_0 else None

    if del_r.any():
        return np.linalg.inv(r0 + p_sph * np.linalg.inv(del_r + Q_sph) + p_sphd * np.linalg.inv(del_r + Q_sphd))
    else:
        return np.linalg.inv(r0)
