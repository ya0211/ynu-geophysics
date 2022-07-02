import pathlib
import random
import matplotlib.pyplot as plt
from utils import *


def draw(_x, _y, display=0):
    plt.figure(figsize=(7, 4))
    plt.subplots_adjust(hspace=0.5)
    plt.title('ex2')
    plt.plot(_x, _y, 'black')

    file_name = out_dir.joinpath("out.pdf")
    plt.savefig(file_name, format="pdf")

    if display != 0:
        plt.show()
    else:
        plt.close()


if __name__ == "__main__":
    out_dir = pathlib.Path("out")

    if not pathlib.Path.exists(out_dir):
        pathlib.Path.mkdir(out_dir)

    x = [1, 2, 4, 3, 6]
    x_index = [0, 4]
    y = [2, 1, 5, 7]
    y_index = [-2, 1]

    print("X: {0}".format(x))
    print("Y: {0}".format(y))
    print("SUM: {0}".format(multipy_then_add(x, y)))

    sum_index = [x_index[0]+y_index[0], x_index[1]+y_index[1]]
    n = []
    for i in range(sum_index[0], sum_index[1]+1):
        n.append(i)

    draw(n, multipy_then_add(x, y), display=1)
