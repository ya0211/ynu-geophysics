from digitalSignal import darray, dft
from digitalSignal.utils import draw
import numpy as np


def func1(n: int) -> float:
    return np.cos(0.355*np.pi*n) + np.cos(0.375*np.pi*n)


def func2(n: int) -> float:
    return np.cos(0.355*np.pi*n) + np.cos(0.5*np.pi*n)


x1_64 = darray([range(0, 64), [func1(i) for i in range(0, 64)]])
x2_64 = darray([range(0, 64), [func2(i) for i in range(0, 64)]])

x1_64_0 = darray([range(0, 128), [func1(i) for i in range(0, 64)]+[0]*64])
x2_64_0 = darray([range(0, 128), [func2(i) for i in range(0, 64)]+[0]*64])

x1_128 = darray([range(0, 128), [func1(i) for i in range(0, 128)]])
x2_128 = darray([range(0, 128), [func2(i) for i in range(0, 128)]])

text = [r'$x_{1}(n)$', r'$x_{2}(n)$']
text += [r'$\left | X_{1}(k) \right |$, 64 sample points']
text += [r'$\left | X_{2}(k) \right |$, 64 sample points']
text += [r'$\left | X_{1}(k) \right |$, 64 sample points, 64 zeros']
text += [r'$\left | X_{2}(k) \right |$, 64 sample points, 64 zeros']
text += [r'$\left | X_{1}(k) \right |$, 128 sample points']
text += [r'$\left | X_{2}(k) \right |$, 128 sample points']

ylabel = [r'$x_{1}(n)$', r'$x_{2}(n)$']
ylabel += [r'$\left | X_{1}(k) \right |$', r'$\left | X_{2}(k) \right |$']*3

xlabel = [r'n', r'n']
xlabel += [r'k', r'k']*3

a = [x1_64, x2_64]
a += [abs(dft(x1_64, k=range(0, 32))), abs(dft(x2_64, k=range(0, 32)))]
a += [abs(dft(x1_64_0, k=range(0, 64))), abs(dft(x2_64_0, k=range(0, 64)))]
a += [abs(dft(x1_128, k=range(0, 64))), abs(dft(x2_128, k=range(0, 64)))]

draw(a=a,
     text=text,
     xlabel=xlabel,
     ylabel=ylabel,
     fig_size=(9, 12),
     style="stem",
     grid='--',
     file_name="figure1.pdf")
