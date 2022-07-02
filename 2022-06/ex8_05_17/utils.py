import numpy as np
import matplotlib.pyplot as plt


class F:
    def __init__(self, x: list, n=None):
        self.x = x[1]
        if n is None:
            self.n = len(self.x)
        else:
            self.n = n
            if n > len(self.x):
                self.x += [i*0 for i in range(0, n-len(self.x))]
            else:
                pass

    def dfs(self, k: int) -> complex:
        real, imag = 0, 0
        for index in range(0, self.n):
            real += self.x[index] * np.cos(2 * np.pi * index * k / self.n)
            imag -= self.x[index] * np.sin(2 * np.pi * index * k / self.n)

        return complex(round(real, 3), round(imag, 3))

    def dfs_abs(self, k: int) -> float:
        dfs_complex = self.dfs(k)
        return np.sqrt(dfs_complex.real ** 2 + dfs_complex.imag ** 2)


def dfs(x, k, n=None):
    return F(x, n).dfs(k)


def dfs_abs(x, k, n=None):
    return F(x, n).dfs_abs(k)


def convolution(x: list, h: list, ll=None) -> list[list, list]:
    n_x, x = x
    n_h, h = h
    tmp_list = list()
    n_target = range(n_x[0] + n_h[0], n_x[-1] + n_h[-1] + 1)

    if len(x) >= len(h):
        be, af = x, h
    else:
        be, af = h, x

    for index in range(-1, -len(af) - 1, -1):
        list_multipy = list()

        if len(af) + index != 0:
            [list_multipy.append(0) for _ in range(0, len(af) + index)]

        [list_multipy.append(n * af[index]) for n in be]

        if -index - 1 != 0:
            [list_multipy.append(0) for _ in range(0, -index - 1)]

        tmp_list.append(list_multipy)

    y_target = [sum([tmp_list[j][i] for j in range(0, len(tmp_list))]) for i in range(0, len(tmp_list[0]))]

    if ll is not None:
        y_target_ll = list()
        for index in range(0, len(y_target[:ll])):
            if index in range(0, len(y_target[ll:])):
                y_target_ll.append(y_target[:ll][index]+y_target[ll:][index])
            else:
                y_target_ll.append(y_target[:ll][index])
        return [n_target[:ll], y_target_ll]
    else:
        return [n_target, y_target]


def draw(x_y: list, text: list, fig_size, style, file_name):
    plt.figure(figsize=fig_size)
    plt.subplots_adjust(hspace=0.5)

    def draw_fun(data, line_style):
        if line_style == "stem":
            plt.stem(data[0], data[1], markerfmt='C0.', bottom=0)
        elif line_style == "plot":
            plt.plot(data[0], data[1])

    for i in range(0, len(x_y)):
        if len(x_y) <= 3:
            plt.subplot(3, 1, i+1)
        elif len(x_y) <= 8:
            plt.subplot(int(np.ceil(len(x_y)/2)), 2, i+1)
        plt.title(text[i])

        if isinstance(style, list):
            draw_fun(x_y[i], style[i])
        elif isinstance(style, str):
            draw_fun(x_y[i], style)

    plt.savefig(file_name)
    plt.close()
