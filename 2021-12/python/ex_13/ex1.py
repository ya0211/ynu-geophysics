import numpy as np
from sympy import *


def fun_3(x, y):  # 三点公式
    h, dy = [x[1] - x[0], []]
    for i in range(0, len(x)):
        if i < 2:  # 输入初始时的两个值
            if i == 0:
                dy.append((-3 * y[i] + 4 * y[i+1] - y[i+2]) / (2 * h))
                dy.append((-y[i] + y[i+2]) / (2 * h))
            else:
                continue
        elif i > len(x)-3:  # 输入结束时的两（一）个值
            if i == len(x)-1:
                if len(x) != 3:  # 修正当len(x)==3（列表x的元素个数等于3）时，重复添加中间值！
                    dy.append((-y[i-2] + y[i]) / (2 * h))
                dy.append((y[i-2] - 4 * y[i-1] + 3 * y[i]) / (2 * h))
            else:
                continue
        else:
            dy.append((-y[i-1] + y[i+1]) / (2 * h))

    return dy


def fun_5(x, y):  # 五点公式
    h, dy = [x[1] - x[0], []]
    for i in range(0, len(x)):
        if i < 3:  # 输入初始时的三个值
            if i == 0:
                dy.append((-25 * y[i] + 48 * y[i+1] - 36 * y[i+2] + 16 * y[i+3] - 3 * y[i+4]) / (12 * h))
                dy.append((-3 * y[i] - 10 * y[i+1] + 18 * y[i+2] - 6 * y[i+3] + y[i+4]) / (12 * h))
                dy.append((y[i] - 8 * y[i+1] + 8 * y[i+3] - y[i+4]) / (12 * h))
            else:
                continue
        elif i > len(x) - 4:  # 输入结束时的三（两）个值
            if i == len(x) - 1:
                if len(x) != 5:  # 修正当len(x)==5（列表x的元素个数等于5）时，重复添加中间值！
                    dy.append((y[i-4] - 8 * y[i-3] + 8 * y[i-1] - y[i]) / (12 * h))
                dy.append((-y[i-4] + 6 * y[i-3] - 18 * y[i-2] + 10 * y[i-1] + 3 * y[i]) / (12 * h))
                dy.append((3 * y[i-4] - 16 * y[i-3] + 36 * y[i-2] - 48 * y[i-1] + 25 * y[i]) / (12 * h))
            else:
                continue
        else:
            dy.append((y[i-2] - 8 * y[i-1] + 8 * y[i+1] - y[i+2]) / (12 * h))

    return dy


def test1():  # 例题测试
    x, y = [[], []]
    for num in np.arange(0.1, 0.7, 0.1):
        x.append(num)
        y.append(np.exp(num) + num)

    return fun_3(x, y), fun_5(x, y)


def ex1():  # EX01
    x, y = [[], []]
    for num in np.arange(1.0, 1.5, 0.1):
        x.append(num)
        y.append(1 / (1 + num) ** 2)

    return fun_3(x, y), fun_5(x, y)


def derivative():  # 借助库sympy（https://www.sympy.org）实现函数求导！
    x = symbols('x')
    f = 1/(1+x)**2
    df = diff(f, x)
    return df


if __name__ == "__main__":
    value = []
    for n in np.arange(1.0, 1.5, 0.1):
        value.append(derivative().evalf(subs={'x': n}))
    print("value :", value)

    dy_1, dy_2 = ex1()
    print("fun_3 :", dy_1)
    print("fun_5 :", dy_2)
