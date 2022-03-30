import math
import numpy as np


def judge(x, parameter_u):
    for j in range(0, len(x)):
        if parameter_u < x[j]:
            return j


def coefficient_a(k, j, x, parameter_u):
    a = 1
    if j <= len(x)-2:
        for c in range(j-1, j+2):
            if k != c:
                a = a * (parameter_u - x[c]) / (x[k] - x[c])
        return a


def function_y(num):
    return math.cos(num)


def main(parameter_u, parameter_x, parameter_y):
    i = judge(parameter_x, parameter_u)
    if abs(parameter_u - parameter_x[i]) > abs(parameter_u - parameter_x[i - 1]):
        i = i - 1
    y = 0
    for e in range(i - 1, i + 2):
        y = y + coefficient_a(e, i, parameter_x, parameter_u) * parameter_y(parameter_x[e])
    return i, y


if __name__ == "__main__":
    array_x = []
    for n in np.arange(0, 8, 8 / 1000):
        array_x.append(n)

    u = 7 * math.pi / 4
    ii, yu = main(u, array_x, function_y)

    print('u = ' + str(u) + '\n' + 'i = ' + str(ii))
    print('y(u) = ' + str(yu) + '\n' + 'cos(u) = ' + str(math.cos(u)))
    print('|yu-cos(u)| =', abs(yu - math.cos(u)))


'''
a1 = (u-x[i])*(u-x[i+1])/((x[i-1]-x[i])*(x[i-1]-x[i+1]))
a2 = (u-x[i-1])*(u-x[i+1])/((x[i]-x[i-1])*(x[i]-x[i+1]))
a3 = (u-x[i-1])*(u-x[i])/((x[i+1]-x[i-1])*(x[i+1]-x[i]))
# yu = a1*y(x[i-1]) + a2*y(x[i]) + a3*y(x[i+1])
'''
