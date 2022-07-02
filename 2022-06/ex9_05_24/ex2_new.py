from digitalSignal import darray, dft
from digitalSignal.utils import draw
import numpy as np


def func(t: int) -> float:
    return np.sin(180 * np.pi * t) + 1.3 * np.sin(260 * np.pi * t) + 1.6 * np.sin(640 * np.pi * t)


def sampling(n: int, fun, fs: float):
    return fun(n/fs)


x = darray([range(0, 64), [sampling(n, func, fs=600) for n in range(0, 64)]])
draw(a=[x, dft.abs(x)],
     text=[r'$x(n)$', r'$\left | X(k) \right |$'],
     xlabel=[r'n', r'k'],
     ylabel=[r'$x(n)$', r'$\left | X(k) \right |$'],
     fig_size=(9, 12),
     style="stem",
     grid='--',
     file_name="figure2-new.pdf")
