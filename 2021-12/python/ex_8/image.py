import math
import matplotlib.pyplot as plt
import numpy as np


def f(n, i):
    if i == 1:
        return math.exp(2*n)+n-4
    if i == 2:
        return math.sin(n/2)+n/2
    if i == 3:
        return n**3+2*n**2+10*n-20


def main(k):
    x, y = [[], []]
    for num in np.arange(0, 10, 0.1):
        x.append(num)
        y.append(f(num, k))
    x = np.array(x)
    y = np.array(y)

    plt.subplot(3, 1, k)
    if k == 1:
        plt.title("y=e^2x+x-4")
    if k == 2:
        plt.title("y=sin(x/2)-x/2")
    if k == 3:
        plt.title("y=x^3+2x^2+10x-20")
    plt.plot(x, y, 'r')


if __name__ == "__main__":
    plt.figure(figsize=(5, 9))
    plt.subplots_adjust(hspace=0.3)

    for j in range(1, 4):
        main(j)
    plt.savefig(fname="image.pdf", format="pdf")
    plt.show()
