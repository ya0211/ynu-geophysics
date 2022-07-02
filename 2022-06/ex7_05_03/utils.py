import matplotlib.pyplot as plt
from math import ceil


def expand(x_n: list, n: int, t: int) -> list:
    _n, _x = x_n
    if _n[0] != 0:
        x_n = t0(x_n)
        _n, _x = x_n
    if len(_x) <= n:
        zero = [z*0 for z in range(0, n - len(_x))]
        _x = _x + zero
    else:
        _x_before, _x_after = _x[0:n], _x[n:len(_x)]
        _x = [_x_before[i] + _x_after[i] for i in range(0, len(_x_after))]
        _x += _x_before[len(_x_after):len(_x_before)]
    _x_expand = list()
    for _ in range(0, t):
        _x_expand += _x
    _n_expand = range(0, len(_x_expand))
    return [_n_expand, _x_expand]


def expand_r(x_n: list, n: int) -> list:
    return expand(x_n, n, 1)


def r(n: int, t: int) -> int:
    if t in range(0, n):
        return 1
    else:
        return 0


def reverse(x_n: list) -> list:
    _n, _x = x_n
    _n_reverse = range(-_n[-1], _n[0]+1)
    _x_reverse = [_x[i] for i in range(-1, -len(_x)-1, -1)]
    return t0([_n_reverse, _x_reverse])


def shift(x_n: list, n) -> list:
    _n, _x = x_n
    _n_shift = range(_n[0]+n, _n[-1]+1+n)
    _x_shift = _x
    return t0([_n_shift, _x_shift])


def t0(x_n: list):
    _n, _x = x_n
    _t = len(_n)
    _n_t0 = range(0, _t)
    _x_t0 = [_x.index(_n.index(0))]
    _x_t0 += [_x[_n.index(i-_t)] for i in range(1, _t)]
    return [_n_t0, _x_t0]


def draw(_x_y: list, _text: list, file_name, style: str or list):
    if len(_x_y) <= 4:
        plt.figure(figsize=(12, 9))
    else:
        plt.figure(figsize=(9, 12))
    plt.subplots_adjust(hspace=0.5)

    for i in range(0, len(_x_y)):
        if len(_x_y) <= 3:
            plt.subplot(3, 1, i+1)
        elif len(_x_y) <= 8:
            plt.subplot(ceil(len(_x_y)/2), 2, i+1)
        plt.title(_text[i])

        if isinstance(style, list):
            if style[i] == "stem":
                plt.stem(_x_y[i][0], _x_y[i][1], markerfmt='C0.')
            elif style[i] == "plot":
                plt.plot(_x_y[i][0], _x_y[i][1])
        elif isinstance(style, str):
            if style == "stem":
                plt.stem(_x_y[i][0], _x_y[i][1], markerfmt='C0.')
            elif style == "plot":
                plt.plot(_x_y[i][0], _x_y[i][1])

    plt.savefig(file_name)
    plt.close()
