import matplotlib.pyplot as plt


def function_l(n, j, num_x, array_x):
    value_l = 1
    for i in range(0, n + 1):
        if i != j:
            value_l = value_l * ((num_x - array_x[i]) / (array_x[j] - array_x[i]))
    return value_l


def coefficient_a(n, j, num_x, array_x):
    value_t = 0
    for i in range(0, n + 1):
        if i != j:
            value_t = value_t + 1 / (array_x[j] - array_x[i])
    value_a = (1 - 2 * (num_x - array_x[j]) * value_t) * (function_l(n, j, num_x, array_x)) ** 2
    return value_a


def coefficient_b(n, j, num_x, array_x):
    value_b = (num_x - array_x[j]) * (function_l(n, j, num_x, array_x)) ** 2
    return value_b


def function_h(num_x, array_x, array_y, array_dy):
    n = len(array_x) - 1  # 根据传入参数自行确定使用几次Hermite插值
    value_h = 0
    for j in range(0, n + 1):
        value_h = value_h + array_y[j] * coefficient_a(n, j, num_x, array_x) + \
                  array_dy[j] * coefficient_b(n, j, num_x, array_x)
    return value_h


if __name__ == "__main__":
    '''
    x = [1.3, 1.6, 1.9]
    y = [0.620086, 0.4554022, 0.2818186]
    dy = [-0.5220232, -0.5698959, -0.5811571]
    '''
    '''
    x = [1, 2]
    y = [2, 3]
    dy = [1, -1]
    '''

    x = [0, 1, 2]
    y = [1, 2.718, 2.389]
    dy = [1, 2.718, 2.389]

    x1 = 1.5
    y1 = function_h(x1, x, y, dy)
    print("f(x1) =", y1)

    x.insert(2, x1)
    y.insert(2, y1)
    print("x:", x, "y:", y)

    plt.figure(figsize=(9, 6))
    plt.plot(x, y, 'r')
    plt.savefig('ex1.pdf', format='pdf')
    plt.show()
