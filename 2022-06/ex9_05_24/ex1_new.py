from digitalSignal import darray, dft
from digitalSignal.utils import draw
import numpy as np


def func(n: int) -> float:
    return np.cos(0.48 * np.pi * n) + np.cos(0.52 * np.pi * n)


x = darray([range(0, 11), [func(i) for i in range(0, 11)]])
draw(a=[x, dft.abs(x)],
     text=[r'$x(n)$', r'$\left | X(k) \right |$'],
     xlabel=[r'n', r'k'],
     ylabel=[r'$x(n)$', r'$\left | X(k) \right |$'],
     fig_size=(9, 12),
     style=["stem", "plot"],
     grid='--',
     file_name="figure1-1-new.pdf")

draw(a=[x, dft.abs(x, n=101)],
     text=[r'$x(n)$', r'$\left | X(k) \right |$'],
     xlabel=[r'n', r'k'],
     ylabel=[r'$x(n)$', r'$\left | X(k) \right |$'],
     fig_size=(9, 12),
     style="plot",
     grid='--',
     file_name="figure1-2-new-1.pdf")

x = darray([range(0, 101), [func(i) for i in range(0, 101)]])
draw(a=[x, dft.abs(x)],
     text=[r'$x(n)$', r'$\left | X(k) \right |$'],
     xlabel=[r'n', r'k'],
     ylabel=[r'$x(n)$', r'$\left | X(k) \right |$'],
     fig_size=(9, 12),
     style="plot",
     grid='--',
     file_name="figure1-3-new.pdf")
