import numpy as np
import matplotlib.pyplot as plt


def get_data(file_name):
    data_x, data_y = [[], []]
    with open(file_name, 'r') as file:
        data = file.readlines()
    for i in range(0, len(data)):
        data_x.append(float(data[i][5:12]))
        data_y.append(float(data[i][14:21]))
    return data_x, data_y


def get_image(file_name, title, num):
    x, y = get_data(file_name)
    x = np.array(x)
    y = np.array(y)

    plt.subplot(3, 1, num)
    plt.title(title)
    plt.plot(x, y, 'black')


if __name__ == "__main__":
    file = ['oridata', 'decdata', 'decdata1']

    plt.figure(figsize=(8, 9))
    plt.subplots_adjust(hspace=0.4)
    for j in range(0, 3):
        file_ = 'data/' + str(file[j]) + '.dat'
        get_image(file_, file[j], j + 1)

    plt.savefig(fname='data/data.pdf', format='pdf')
    plt.show()
