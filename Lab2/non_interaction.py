from nia_scheme import calculate_effective_conductivity, calculate_effective_conductivity_dual
import matplotlib.pyplot as plt

"""
В рамках метода гомогенизации без учета взаимодействия неоднородностей
(NIA) определить эффективную теплопроводность двухфазного материала,
состоящего из матрицы с теплопроводностью k0 и двух типов
неоднородностей с теплопроводностью k1 (k_1 / k_0 = alpha - известная величина),
имеющих разную форму: часть неоднородностей имеет сферическую форму,
часть неоднородностей имеет форму сфероидов с заданным соотношением
длин полуосей a_3 / a = gamma (a_1 = a_2 = a). При этом все сфероидальные
неоднородности ориентированы строго параллельно друг другу. Рассмотреть
следующие варианты геометрии микроструктуры:
a) pсфероидов = pсфер = p/2,
b) pсфероидов = 0, pсфер = p,
c) pсфероидов = p, pсфер = 0,
где p – суммарная объемная доля неоднородностей.
Провести анализ зависимостей
k_ii / k_0 (i = 1, 2, 3) от объемной доли p.
"""

if __name__ == '__main__':
    k_0 = 200
    alpha = 0.2
    k_1 = alpha * k_0
    m = [1, 0, 0]
    gamma = 0.8
    type_inh = 1
    k_11, k_22, k_33 = [], [], []
    k_11_dual, k_22_dual, k_33_dual = [], [], []
    p_1_list = [i / 100 for i in range(0, 101)]
    for p_1 in p_1_list:
        k_eff = calculate_effective_conductivity(p_1, type_inh, k_0, k_1, m, gamma)
        k_eff_dual = calculate_effective_conductivity_dual(p_1, type_inh, k_0, k_1, m, gamma)
        k_11.append(k_eff[0][0] / k_0)
        k_22.append(k_eff[1][1] / k_0)
        k_33.append(k_eff[2][2] / k_0)
        k_11_dual.append(k_eff_dual[0][0] / k_0)
        k_22_dual.append(k_eff_dual[1][1] / k_0)
        k_33_dual.append(k_eff_dual[2][2] / k_0)

    fig, axs = plt.subplots(1, 3, figsize=(10, 8))
    type_map = {
        1: r'Spheres and spheroids with $\gamma = $' + f'{gamma}',
        2: 'Only spheres',
        3: r'Only spheroids with $\gamma = $' + f'{gamma}',
    }
    fig.suptitle(r'Effective Conductivity with $k_0$ = ' + f'{k_0}' +r', $k_1$ = ' + f'{k_1}; {type_map[type_inh]}.', fontsize=16)
    axs[0].plot(p_1_list, k_11, label='NIA', color='pink')
    axs[0].plot(p_1_list, k_11_dual, label='Dual NIA', color='green')
    axs[0].set_xlabel('p')
    axs[0].set_ylabel(r'$\frac{k^{eff}_{11}}{k_0}$')
    axs[0].legend()
    axs[0].grid(True, color='gray', linestyle='--', linewidth=0.5)

    axs[1].plot(p_1_list, k_22, label='NIA', color='pink')
    axs[1].plot(p_1_list, k_22_dual, label='Dual NIA', color='green')
    axs[1].set_xlabel('p')
    axs[1].set_ylabel(r'$\frac{k^{eff}_{22}}{k_0}$')
    axs[1].legend()
    axs[1].grid(True, color='gray', linestyle='--', linewidth=0.5)

    axs[2].plot(p_1_list, k_33, label='NIA', color='pink')
    axs[2].plot(p_1_list, k_33_dual, label='Dual NIA', color='green')
    axs[2].set_xlabel('p')
    axs[2].set_ylabel(r'$\frac{k^{eff}_{33}}{k_0}$')
    axs[2].legend()

    axs[2].grid(True, color='gray', linestyle='--', linewidth=0.5)
    # Настройка отступов
    plt.tight_layout()
    plt.show()
