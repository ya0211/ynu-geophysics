import os.path

import numpy as np
import matplotlib.pyplot as plt
import image
import ex1


def n(tmp_x):
    for i in range(0, len(tmp_x)):
        if tmp_x[i] > 1:
            return i


def draw(tmp_x, tmp_y):
    plt.figure(figsize=(8, 9))
    plt.subplots_adjust(hspace=0.4)
    title = ['out.dat', 'decdata.dat', 'oridata.dat']
    for i in range(0, 3):
        plt.subplot(3, 1, i + 1)
        plt.title(title[i])
        if i != 0:
            tmp_x, tmp_y = image.get_data('data/' + str(title[i]))

        i = n(tmp_x)
        tmp_x = tmp_x[:i]
        tmp_y = tmp_y[:i]
        plt.plot(tmp_x, tmp_y, 'black')

    plt.savefig(fname='out.pdf', format='pdf')
    plt.show()


def add(tmp_u, tmp_yu, tmp_j, tmp_data_x, tmp_data_y, tmp_array_x, tmp_array_y):
    if tmp_yu is not None:
        tmp_data_x.append(tmp_array_x[tmp_j])
        tmp_data_x.append(round(tmp_u, 3))

        tmp_data_y.append(tmp_array_y[tmp_j])
        tmp_data_y.append(round(tmp_yu, 3))


def main(parameter_u, parameter_x, parameter_y):
    i = ex1.judge(parameter_x, parameter_u)
    if i is not None:
        if abs(parameter_u - parameter_x[i]) > abs(parameter_u - parameter_x[i - 1]):
            i = i - 1
        y = 0
        for e in range(i - 1, i + 2):
            a = ex1.coefficient_a(e, i, parameter_x, parameter_u)
            if a is not None:
                y = y + a * parameter_y[e]
        return y


if __name__ == "__main__":
    file_name = 'data/decdata.dat'
    array_x, array_y = image.get_data(file_name)

    dt = 0.4
    if os.path.exists('out.dat'):
        os.system('rm out.dat')
    for value in [-4.84, -4.94]:
        data_x, data_y, j = [[], [], 0]
        for u in np.arange(value, 40.0, dt):
            yu = main(u, array_x, array_y)
            add(u, yu, j, data_x, data_y, array_x, array_y)
            j += 1
        dt = dt - 0.2
        array_x, array_y = data_x, data_y

    for k in range(0, len(data_x)):
        with open('out.dat', 'a') as file:
            file.write(str(data_x[k]) + '      ' + str(data_y[k]) + '\n')

    draw(data_x, data_y)
