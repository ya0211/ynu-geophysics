from fourier_transform import FourierTransform
import matplotlib.pyplot as plt
import numpy as np


def draw(_x, _y, text, file_name, display=1):

    plt.figure(figsize=(9, 12))
    plt.subplots_adjust(hspace=0.5)

    plt.subplot(3, 1, 1)
    plt.title(text[0])
    plt.xlabel('n')
    plt.xticks(range(-5, 6))
    plt.stem(_x[0], _y[0], markerfmt='C0.')

    plt.subplot(3, 1, 2)
    plt.title(text[1])
    plt.xlabel('k')
    plt.xticks(range(-5, 6))
    plt.plot(_x[1][1], _y[1][1], 'red', linestyle='--')
    plt.stem(_x[1][0], _y[1][0], markerfmt='C0.')

    plt.savefig(file_name, format="pdf")

    if display != 0:
        plt.show()
    else:
        plt.close()


def r(_n, _i):
    if _i in range(0, _n):
        return 1
    else:
        return 0


def x(_n):
    _x = 0
    for _i in range(int(-_n/5), int((4-_n)/5)+1):
        _x += r(5, _n+5*_i)
    return _x


if __name__ == "__main__":
    x = [x(i) for i in np.arange(-5, 6)]

    f = FourierTransform(x, n=5)
    x_f = [f.dfs_abs(k) for k in np.arange(-5, 6)]
    x_f_w = [f.dfs_abs(k) for k in np.arange(-5, 5, 0.01)]

    draw([np.arange(-5, 6), [np.arange(-5, 6), np.arange(-5, 5, 0.01)]],
         [x, [x_f, x_f_w]], ['x(n)', 'X(k) and X(w)'], '3.1.pdf', display=0)
