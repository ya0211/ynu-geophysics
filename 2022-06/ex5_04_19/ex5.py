import numpy as np
import matplotlib.pyplot as plt


def fun():
    return lambda t: 5 * np.cos(2 * np.pi * t) \
                     - 3 * np.cos(3 * np.pi * t) \
                     + 2 * np.cos(6 * np.pi * t) \
                     + np.cos(8 * np.pi * t)


def draw(_x, _y, text, file_name, display=1):
    color = {0: 'black', 1: 'red', 2: 'blue'}

    plt.figure(figsize=(9, 11))
    plt.subplots_adjust(hspace=0.5)

    for _i in range(0, len(_x)):
        plt.subplot(len(_x), 1, _i+1)
        plt.grid(linestyle='--', linewidth=1)
        plt.title(text[_i])
        if _i == 0:
            plt.ylabel('x(t)')
            plt.xlabel('t')
            plt.plot(_x[_i], _y[_i], color.get(_i))
        else:
            plt.ylabel('x(n)')
            plt.xlabel('n')
            plt.stem(_x[_i], _y[_i], markerfmt='C0.')

    plt.savefig(file_name, format="pdf")

    if display != 0:
        plt.show()
    else:
        plt.close()


def main(func, fs, _max):
    _x, _y, _n = [[], [], range(0, _max * fs)]
    for _i in _n:
        _x.append(_i / fs)
        _y.append(func(t=_i / fs))
    return _x, _n, _y


if __name__ == "__main__":
    x1, _, y1 = main(func=fun(), fs=100, _max=4)
    _, n2, y2 = main(func=fun(), fs=12, _max=4)
    _, n3, y3 = main(func=fun(), fs=20, _max=4)

    draw([x1, n2, n3], [y1, y2, y3], ['xa(t)', 'fs=12Hz', 'fs=20Hz'], "1.pdf")
