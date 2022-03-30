import numpy as np
import matplotlib.pyplot as plt


def fx_1(tmp_x, tmp_y, j):  # 计算一阶差商，并返回值
    return (tmp_y[j] - tmp_y[j-1])/(tmp_x[j] - tmp_x[j-1])


def fx_2(tmp_x, tmp_y, j):  # 调用一阶差商fx_1(tmp_x, tmp_y, j)，生成二阶差商，并返回值
    return (fx_1(tmp_x, tmp_y, j) - fx_1(tmp_x, tmp_y, j-1))/(tmp_x[j] - tmp_x[j-2])


def fx_3(tmp_x, tmp_y, j):  # 调用二阶差商fx_2(tmp_x, tmp_y, j)，生成三阶差商，并返回值
    return (fx_2(tmp_x, tmp_y, j) - fx_2(tmp_x, tmp_y, j-1))/(tmp_x[j] - tmp_x[j-3])


def fx_4(tmp_x, tmp_y, j):  # 调用三阶差商fx_3(tmp_x, tmp_y, j)，生成四阶差商，并返回值
    return (fx_3(tmp_x, tmp_y, j) - fx_3(tmp_x, tmp_y, j-1))/(tmp_x[j] - tmp_x[j-4])


def nx(tmp_x, tmp_y, num_x):  # 生成四次插值公式，计算输入的num_x的nx(num_x)值， 并返回值
    x_value = 1
    n_value = tmp_y[0]
    fx = [fx_1, fx_2, fx_3, fx_4]
    for j in range(0, 4):
        x_value = x_value*(num_x - tmp_x[j])
        n_value = n_value + fx[j](tmp_x, tmp_y, j+1)*x_value
    return n_value


if __name__ == "__main__":
    array_x = []
    for num in np.arange(0.125, 0.875, 0.125):  # 生成x值输入列表array_x
        array_x.append(num)

    array_y = [0.796, 0.773, 0.744, 0.704, 0.656, 0.602]  # 定义列表array_y，赋值f(x)

    x1 = 0.158
    x2 = 0.638
    y1 = nx(array_x, array_y, x1)  # 调用函数nx(tmp_x, tmp_y, num_x)，计算f(x)值
    y2 = nx(array_x, array_y, x2)
    print("f(0.158) =", y1)
    print("f(0.638) =", y2)

    # 将x1, x2添加到列表array_x
    array_x.append(x1)
    array_x.append(x2)
    array_x.sort()

    for i in range(0, len(array_x)):  # 判断x1 ,x2在列表的位置，将y1, y2添加到对应位置
        if array_x[i] == x1:
            array_y.insert(i, y1)
        if array_x[i] == x2:
            array_y.insert(i, y2)

    # 作图
    array_x = np.array(array_x)
    array_y = np.array(array_y)

    plt.figure(figsize=(9, 6))
    plt.plot(array_x, array_y, 'r')
    plt.savefig(fname='ex1.pdf', format='pdf')
    plt.show()
