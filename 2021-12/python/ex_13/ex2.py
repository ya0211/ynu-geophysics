import numpy as np
import ex1
from sympy import *


def derivative():
    x = symbols('x')
    f = -cot(x)
    df = diff(f, x)
    return df


def main(value):
    for h in [0.001, 0.002, 0.005, 0.010, 0.020, 0.050, 0.1]:
        x, y = [[], []]
        for num in [0.04 - h, 0.04, 0.04 + h]:
            x.append(num)
            y.append(-1 / np.tan(num))
        dy = ex1.fun_3(x, y)

        print("h=" + str(h) + " : " + str(dy[1]) + ", |∆|=" + str(abs(dy[1]-value)))


if __name__ == "__main__":
    real_value = derivative().evalf(subs={'x': 0.04})
    print("value: " + str(real_value))
    main(real_value)
