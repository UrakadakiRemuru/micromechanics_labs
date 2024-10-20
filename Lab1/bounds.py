from random import randint

from matplotlib import pyplot as plt

def voigt_reuss_bounds_conductivity(k_0: float, k_1: float) -> dict:
    volume_fraction_of_inhomo = [i / 100 for i in range(0, 101)]

    k_v, k_r = [], []

    for p in volume_fraction_of_inhomo:
        k_v.append((k_0 * (1 - p) + k_1 * p) / k_0)
        k_r.append(((1 - p) / k_0 + p / k_1) ** (-1) / k_0)

    return {
        'bound_1': k_v,
        'colour_1': 'pink',
        'label_name_1': 'Voigt',
        'bound_2': k_r,
        'colour_2': 'blue',
        'label_name_2': 'Reuss',
        'volume_fraction': volume_fraction_of_inhomo,
        'name': f'Conductivity Voigt-Reuss bounds with $k_0$ = {k_0} and $k_1$ = {k_1}'
    }


def voigt_reuss_bounds_elasticity(k_0: float, k_1: float, m_0: float, m_1: float) -> dict:
    volume_fraction_of_inhomo = [i / 100 for i in range(0, 101)]

    k_v, k_r, m_v, m_r = [], [], [], []

    for p in volume_fraction_of_inhomo:
        k_v.append((k_0 * (1 - p) + k_1 * p) / k_0)
        k_r.append(((1 - p) / k_0 + p / k_1) ** (-1) / k_0)

        m_v.append((m_0 * (1 - p) + m_1 * p) / m_0)
        m_r.append(((1 - p) / m_0 + p / m_1) ** (-1) / m_0)

    return {
        'k': {
            'bound_1': k_v,
            'colour_1': 'pink',
            'bound_2': k_r,
            'colour_2': 'blue',
            'volume_fraction': volume_fraction_of_inhomo,
            'name': r'Elasticity Voigt-Reuss bounds with $K_0$ = ' + str(k_0) + ' and $K_1$ = ' + str(k_1)
        },
        'm': {
            'bound_1': m_v,
            'colour_1': 'pink',
            'bound_2': m_r,
            'colour_2': 'blue',
            'volume_fraction': volume_fraction_of_inhomo,
            'name': r'Elasticity Voigt-Reuss bounds with $\mu_0$ = ' + str(m_0) + r' and $\mu_1$ = ' + str(m_1)
        }
    }

def hashin_shtrikman_bounds_conductivity(k_0: float, k_1: float) -> dict:
    volume_fraction_of_inhomo = [i / 100 for i in range(0, 101)]

    k_up, k_low = [], []

    for p in volume_fraction_of_inhomo:
        if k_0 > k_1:
            k_up.append((k_0 + p / ((1 - p) / 3 / k_0 + 1 / (k_1 - k_0))) / k_0)
            k_low.append((k_1 + (1 - p) / (p / 3 / k_1 - 1 / (k_1 - k_0))) / k_0)
        else:
            k_low.append((k_0 + p / ((1 - p) / 3 / k_0 + 1 / (k_1 - k_0))) / k_0)
            k_up.append((k_1 + (1 - p) / (p / 3 / k_1 - 1 / (k_1 - k_0))) / k_0)
    print('Upper bound:', k_up)
    print('Lowwer bound:', k_low)
    return {
        'bound_1': k_up,
        'colour_1': 'green',
        'label_name_1': r'$Hashin-Strickman^{+}$',
        'bound_2': k_low,
        'colour_2': 'yellow',
        'label_name_2': r'$Hashin-Strickman^{-}$',
        'volume_fraction': volume_fraction_of_inhomo,
        'name': f'Conductivity Voigt-Reuss and Hashin-Strikman bounds with $k_0$ = {k_0} and $k_1$ = {k_1}'
    }

def draw_bounds_elasticity(data: dict) -> None:
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 4))

    ax1.plot(data['k']['volume_fraction'], data['k']['bound_1'], label='Voigt', linestyle='--', color=data['k']['colour_1'])
    ax1.plot(data['k']['volume_fraction'], data['k']['bound_2'], label='Reuss', linestyle='--',
             color=data['k']['colour_2'])
    ax1.set_title(data['k']['name'])
    ax1.set_xlabel(r'$p$')
    ax1.set_ylabel(r'$\frac{K_{eff}}{K_0}$', fontsize=16)
    ax1.grid(True, color='gray', linestyle='--', linewidth=0.5)
    ax1.legend()

    ax2.plot(data['m']['volume_fraction'], data['m']['bound_1'], label='Voigt', linestyle='--',
             color=data['m']['colour_1'])
    ax2.plot(data['m']['volume_fraction'], data['m']['bound_2'], label='Reuss', linestyle='--',
             color=data['m']['colour_2'])
    ax2.set_title(data['m']['name'])
    ax2.set_xlabel(r'$p$')
    ax2.set_ylabel(r'$\frac{\mu_{eff}}{\mu_0}$', fontsize=16)
    ax2.grid(True, color='gray', linestyle='--', linewidth=0.5)
    ax2.legend()

    plt.show()

def draw_bounds_conductivity(data: list[dict]) -> None:
    for bounds in data:
        plt.plot(bounds['volume_fraction'], bounds['bound_1'], label=bounds['label_name_1'], linestyle='--', color=bounds['colour_1'])
        plt.plot(bounds['volume_fraction'], bounds['bound_2'], label=bounds['label_name_2'], linestyle='-.', color=bounds['colour_2'])
        title_name = bounds['name']

    plt.legend()
    plt.ylabel(r'$\frac{k_{eff}}{k_0}$', fontsize=16)
    plt.xlabel(r'p')
    plt.title(title_name)
    plt.grid(True)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.show()



if __name__ == '__main__':
    k_0, k_1 = 700, 300
    data1 = voigt_reuss_bounds_conductivity(k_0, k_1)
    data2 = hashin_shtrikman_bounds_conductivity(k_0, k_1)
    draw_bounds_conductivity([data1, data2])
    data = voigt_reuss_bounds_elasticity(randint(1, 800), randint(1, 800), randint(1, 200), randint(1, 200))
    draw_bounds_elasticity(data)
