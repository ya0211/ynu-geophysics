from fourier_transform import FourierTransform
import matplotlib.pyplot as plt
import numpy as np


def draw(_x, _y, text, file_name, display=1):

    plt.figure(figsize=(9, 12))
    plt.subplots_adjust(hspace=0.5)

    plt.subplot(3, 1, 1)
    plt.title(text[0])
    plt.xlabel('n')
    plt.xticks(range(-10, 11))
    plt.stem(_x[0], _y[0], markerfmt='C0.')

    plt.subplot(3, 1, 2)
    plt.title(text[1])
    plt.xlabel('k')
    plt.xticks(range(-12, 13))
    plt.plot(_x[1][1], _y[1][1], 'red', linestyle='--')
    plt.stem(_x[1][0], _y[1][0], markerfmt='C0.')

    plt.subplot(3, 1, 3)
    plt.title(text[2])
    plt.xlabel('k')
    plt.xticks(range(-12, 13))
    plt.plot(_x[1][1], _y[2][1], 'red', linestyle='--')
    plt.stem(_x[1][0], _y[2][0], markerfmt='C0.')

    plt.savefig(file_name, format="pdf")

    if display != 0:
        plt.show()
    else:
        plt.close()


def x(n):
    if n in range(0, 5):
        return 1
    if n in range(5, 10):
        return 0


if __name__ == "__main__":
    x = [x(i) for i in np.arange(0, 10)]
    x += x

    f = FourierTransform(x, n=10)
    x_f = [f.dfs_abs(k) for k in np.arange(-12, 13)]
    x_f_w = [f.dfs_abs(k) for k in np.arange(-12, 12, 0.01)]
    x_f_arg = [f.dfs_arg(k) for k in np.arange(-12, 13)]
    x_f_arg_w = [f.dfs_arg(k) for k in np.arange(-12, 12, 0.01)]

    draw([np.arange(-10, 10), [np.arange(-12, 13), np.arange(-12, 12, 0.01)]],
         [x, [x_f, x_f_w], [x_f_arg, x_f_arg_w]],
         ['x(n)', 'X(k) and X(w)', 'arg[X(k)] and arg[X(w)]'], '3.2.pdf', display=0)
