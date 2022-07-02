from digitalSignal import SignalArray
import numpy as np
import matplotlib.pyplot as plt


class F:
    def __init__(self, x: SignalArray, n=None):
        self.x = x[1]
        if n is None:
            self.n = len(self.x)
        else:
            self.n = n
            if n > len(self.x):
                self.x += [i*0 for i in range(0, n-len(self.x))]
            else:
                pass

    def __call__(self, x: SignalArray, n=None):
        self.__init__(x, n)

    def dfs(self, k: int) -> complex:
        real, imag = 0, 0
        for index in range(0, self.n):
            real += self.x[index] * np.cos(2 * np.pi * index * k / self.n)
            imag -= self.x[index] * np.sin(2 * np.pi * index * k / self.n)

        return complex(round(real, 3), round(imag, 3))

    def dfs_abs(self, k: int) -> float:
        dfs_complex = self.dfs(k)
        return np.sqrt(dfs_complex.real ** 2 + dfs_complex.imag ** 2)


def draw(xy: list, text: list, xlabel=None, ylabel=None,
         fig_size=(12, 9), style="plot", grid=None, file_name="figure.pdf"):

    plt.figure(figsize=fig_size)
    plt.subplots_adjust(hspace=0.5)

    def draw_fun(data, draw_style):
        if draw_style == "stem":
            plt.stem(data[0], data[1], markerfmt='C0.')
            bottom, top = plt.ylim()
            if min(data[1]) >= 0:
                plt.ylim(0, top)
            else:
                pass
        elif draw_style == "plot":
            plt.plot(data[0], data[1])

    for i in range(0, len(xy)):
        if len(xy) <= 3:
            plt.subplot(3, 1, i+1)
        elif len(xy) <= 8:
            plt.subplot(int(np.ceil(len(xy)/2)), 2, i+1)
        plt.title(text[i])
        if grid is not None:
            plt.grid(linestyle=grid, linewidth=1)
        if xlabel is not None:
            plt.xlabel(xlabel[i])
        if ylabel is not None:
            plt.ylabel(ylabel[i])

        if isinstance(style, list):
            draw_fun(xy[i], style[i])
        elif isinstance(style, str):
            draw_fun(xy[i], style)

    plt.savefig(file_name)
    plt.close()
