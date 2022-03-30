import numpy as np


def rectangle(x1, x2, fun, n):
    integral, x, d = [0, [], (x2-x1)/n]
    for num in np.arange(x1, x2+d, d):
        x.append(num)
    for i in range(0, n):
        integral = integral + fun(x[i]) * d

    return integral


def trapezoid(x1, x2, fun, n):
    integral, x, d = [0, [], (x2 - x1) / n]
    for num in np.arange(x1, x2 + d, d):
        x.append(num)
    for i in range(0, n + 1):
        if i in [0, n]:
            c = 1 / 2
        else:
            c = 1
        integral = integral + c * fun(x[i]) * d

    return integral


def parabola(x1, x2, fun, n):
    integral, x, d = [0, [], (x2 - x1) / n]
    for num in np.arange(x1, x2 + d, d):
        x.append(num)
    for i in range(0, n + 1):
        if i in [0, n]:
            c = 1 / 3
        elif i % 2 != 0:
            c = 4/3
        else:
            c = 2/3
        integral = integral + c * fun(x[i]) * d

    return integral


if __name__ == "__main__":
    def f(x):
        return np.cos(1/(1+x**2))

    print("rectangle :", rectangle(0, np.pi, f, 1000))
    print("trapezoid :", trapezoid(0, np.pi, f, 1000))
    print("parabola :", parabola(0, np.pi, f, 1000))
