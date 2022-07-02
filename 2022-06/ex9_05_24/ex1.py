import numpy as np
from ex8_05_17.utils import dfs_abs
from ex9_05_24.utils import draw


def x(n: int) -> float:
    return np.cos(0.48 * np.pi * n) + np.cos(0.52 * np.pi * n)


x_n = [range(0, 11), [x(i) for i in range(0, 11)]]
x_n_dfs_abs = [range(0, 11), [dfs_abs(x_n, k) for k in range(0, 11)]]
draw(xy=[x_n, x_n_dfs_abs],
     text=[r'$x(n)$', r'$\left | X(k) \right |$'],
     xlabel=[r'n', r'k'],
     ylabel=[r'$x(n)$', r'$\left | X(k) \right |$'],
     fig_size=(9, 12),
     style=["stem", "plot"],
     grid='--',
     file_name="figure1-1.pdf")

x_n = [range(0, 101), [x(i) for i in range(0, 11)] + [0] * 90]
x_n_dfs_abs = [range(0, 101), [dfs_abs(x_n, k) for k in range(0, 101)]]
draw(xy=[x_n, x_n_dfs_abs],
     text=[r'$x(n)$', r'$\left | X(k) \right |$'],
     xlabel=[r'n', r'k'],
     ylabel=[r'$x(n)$', r'$\left | X(k) \right |$'],
     fig_size=(9, 12),
     style="plot",
     grid='--',
     file_name="figure1-2.pdf")

x_n = [range(0, 101), [x(i) for i in range(0, 101)]]
x_n_dfs_abs = [range(0, 101), [dfs_abs(x_n, k) for k in range(0, 101)]]
draw(xy=[x_n, x_n_dfs_abs],
     text=[r'$x(n)$', r'$\left | X(k) \right |$'],
     xlabel=[r'n', r'k'],
     ylabel=[r'$x(n)$', r'$\left | X(k) \right |$'],
     fig_size=(9, 12),
     style="plot",
     grid='--',
     file_name="figure1-3.pdf")
