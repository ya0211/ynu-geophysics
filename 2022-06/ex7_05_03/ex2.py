from utils import *
from ex2_03_29.utils import multipy_then_add


def x(n: int):
    if n in range(0, 5):
        return n+1
    else:
        return 0


def h(n: int):
    return r(4, n-2)


x_n = [range(0, 6), [x(n) for n in range(0, 6)]]
h_n = [range(0, 6), [h(n) for n in range(0, 6)]]
x_n_6 = expand(x_n, 6, 3)
h_n_6 = expand(h_n, 6, 3)
r = multipy_then_add(x_n_6[1], h_n_6[1]).get('r')
y_n = [range(0, len(r)), r]

x_y = [x_n, x_n_6, h_n, h_n_6, y_n]
text = ['x(n)', 'x((n))_6', 'h(n)', 'h((n))_6', 'x(n)*h(n)']
draw(x_y, text, 'figure2.pdf')
