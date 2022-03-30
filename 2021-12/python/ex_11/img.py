import numpy as np
import matplotlib.pyplot as plt


def get_data(file_name):  # 获取数据
    data_x, data_y = [[], []]
    with open(file_name, 'r') as file:
        data = file.readlines()  # 读取整个文件
    for i in range(0, len(data)):
        data_x.append(float(data[i][4:12]))  # 将第4-12列数据输入列表data_x
        data_y.append(float(data[i][14:21]))  # 将第14-21列数据输入列表data_y
    return data_x, data_y


def n(x):  # 设置作图范围：-10-5
    for i in range(0, len(x)):
        if x[i] == 5:
            return i


def get_image(file_name, title, num):
    x, y = get_data(file_name)
    i = n(x)
    x = np.array(x[:i])  # 列表元素裁断
    y = np.array(y[:i])

    plt.subplot(2, 1, num)  # 设置子图位置
    plt.title(title)
    plt.plot(x, y, 'black')


if __name__ == "__main__":
    plt.figure(figsize=(8, 9))  # 画布大小
    plt.subplots_adjust(hspace=0.4)  # 设置子图之间的间距
    get_image("data/bassum.dat", "bassum.dat", 1)
    get_image("data/bassum_o.dat", "bassum_o.dat", 2)
    plt.savefig(fname='data/data.pdf', format='pdf')
    plt.show()
