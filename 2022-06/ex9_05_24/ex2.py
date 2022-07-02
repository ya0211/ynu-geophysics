import numpy as np
from ex8_05_17.utils import dfs_abs
from ex9_05_24.utils import draw


def x(t: int) -> float:
    return np.sin(180 * np.pi * t) + 1.3 * np.sin(260 * np.pi * t) + 1.6 * np.sin(640 * np.pi * t)


def sampling(n: int, fun, fs: float):
    return fun(n/fs)


x_n = [range(0, 64), [sampling(n, x, fs=600) for n in range(0, 64)]]
x_n_dfs_abs = [range(0, 64), [dfs_abs(x_n, k) for k in range(0, 64)]]
draw(xy=[x_n, x_n_dfs_abs],
     text=[r'$x(n)$', r'$\left | X(k) \right |$'],
     xlabel=[r'n', r'k'],
     ylabel=[r'$x(n)$', r'$\left | X(k) \right |$'],
     fig_size=(9, 12),
     style="stem",
     grid='--',
     file_name="figure2.pdf")
