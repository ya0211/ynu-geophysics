import pathlib
import numpy as np
import matplotlib.pyplot as plt


def fun(flag, a=1):
    function = {1.0: lambda t: np.sin(2 * np.pi * 50 * t + np.pi / 8),
                2.1: lambda t: a * np.cos(2 * np.pi * 125 * t),
                2.2: lambda t: a * np.cos(100 * t),
                2.3: lambda t: np.cos(2 * np.pi * 50 * t) + np.cos(2 * np.pi * 80 * t) + np.cos(2 * np.pi * 180 * t)}
    return function.get(flag)


def draw(_x, _y, text, file_name, display=0):
    out_dir = pathlib.Path("out")
    if not pathlib.Path.exists(out_dir):
        pathlib.Path.mkdir(out_dir)

    color = {0: 'black', 1: 'red'}

    plt.figure(figsize=(9, 11))
    plt.subplots_adjust(hspace=0.5)

    for _i in range(0, len(_x)):
        plt.subplot(2, 1, _i+1)
        plt.title(text[_i])
        plt.plot(_x[_i], _y[_i], color.get(_i))

    file_name = out_dir.joinpath(file_name)
    plt.savefig(file_name, format="pdf")

    if display != 0:
        plt.show()
    else:
        plt.close()


def main(func, fs, _max):
    _x, _y = [[], []]
    for _n in range(0, 10000):
        if _n/fs <= _max:
            _x.append(_n/fs)
            _y.append(func(t=_n/fs))
        else:
            break
    return _x, _y


if __name__ == "__main__":
    """
    1.0 fs=200 max=0.050
    2.1 fs=400 max=0.020
    2.2 fs=400 max=0.200
    2.3 fs=720 max=0.075
    """
    args = [[1.0, 200, 0.050, ['x(t) = sin(2*pi*50t + pi/8)', 'fs=200']],
            [2.1, 400, 0.020, ['x(t) = Acos(2*pi*125t)', 'fs=400']],
            [2.2, 400, 0.200, ['x(t) = Acos(100t)', 'fs=400']],
            [2.3, 720, 0.075, ['x(t) = cos(2*pi*50t)+cos(2*pi*80t)+cos(2*pi*180t)', 'fs=720']]]

    for index in range(0, 4):
        x1, y1 = main(func=fun(args[index][0]), fs=5000, _max=args[index][2])
        x2, y2 = main(func=fun(args[index][0]), fs=args[index][1], _max=args[index][2])

        draw([x1, x2], [y1, y2], args[index][3], "{0}.pdf".format(args[index][0]))
