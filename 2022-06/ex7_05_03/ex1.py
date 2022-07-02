from utils import *

x_n = [range(0, 4), [1, 1, 3, 2]]
"""print("x(n)", x_n)
print("x(-n)", reverse(x_n))
print("x(-n)_t0", t0(reverse(x_n)))
print("x(n-3)", shift(x_n, -3))
print("x(n-3)_t0", t0(shift(x_n, -3)))"""
x__n_5 = expand(reverse(x_n), 5, 5)
x__n_6_r = expand_r(reverse(x_n), 6, 5)
x_n_3_r = expand_r(x_n, 3, 5)
x_n_6 = expand(x_n, 6, 5)
x_n_3_5_r = expand_r(shift(x_n, -3), 5, 5)
x_n_7_r = expand_r(x_n, 7, 5)

x_y = [x_n, x__n_5, x__n_6_r, x_n_3_r, x_n_6, x_n_3_5_r, x_n_7_r]
text = ['x(n)', 'x((-n))_5', 'x((-n))_6 R_6(n)', 'x((n))_3 R_3(n)', 'x((n))_6', 'x((n-3))_5 R_5(n)', 'x((n))_7 R_7(n)']

draw(x_y, text, 'figure1.pdf')
