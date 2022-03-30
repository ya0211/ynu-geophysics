import ex1  # 调用程序ex1.py
import img  # 调用程序img.py
import os.path
import numpy as np
import matplotlib.pyplot as plt


def n(tmp_x):  # 设置作图范围：-10-1
    for i in range(0, len(tmp_x)):
        if tmp_x[i] > 1:
            return i


def judge(tmp_x, tmp_u):  # 判断计算值tmp_u，在列表tmp_x中的位置，返回适当参数j
    for j in range(0, len(tmp_x)):
        if tmp_u < tmp_x[j]:
            if j-2 < 0:  # 修正初始时j取值
                j = j+2
            if j+4 > len(tmp_x):  # 修正结束时j取值
                j = j-4
            return j


def draw(tmp_x, tmp_y):  # 作图
    plt.figure(figsize=(8, 9))  # 画布大小
    plt.subplots_adjust(hspace=0.4)  # 子图间距
    title = ['out.dat', 'bassum.dat', 'bassum_o.dat']
    for k in range(0, 3):
        plt.subplot(3, 1, k+1)
        plt.title(title[k])
        if k != 0:  # 控制bassum.dat, bassum_o.dat值从文件读入
            tmp_x, tmp_y = img.get_data('data/' + str(title[k]))  # 使用img.py中的函数get_data获取数据

        i = n(tmp_x)
        tmp_x = tmp_x[:i]
        tmp_y = tmp_y[:i]
        plt.plot(tmp_x, tmp_y, 'black')

    plt.savefig(fname='ex2.pdf', format='pdf')
    plt.show()


def main(file_path):
    x, y = img.get_data(file_path)  # 使用img.py中的函数get_data获取数据
    array_x, array_y, j = [[], [], 0]
    for num_x in np.arange(-9.9, 39.9, 0.2):  # 生成计算值
        array_x.append(x[j])  # 生成新列表array_x，添加原始数据
        array_x.append(num_x)  # 添加计算数据

        i = judge(x, num_x)  # 调用函数judge(tmp_x, tmp_u)，取得返回值i
        tmp_x = x[i-2:i+4]  # 根据i值截断列表，以生成与函数nx(tmp_x, tmp_y, num_x)匹配列表
        tmp_y = y[i-2:i+4]

        array_y.append(y[j])
        array_y.append(ex1.nx(tmp_x, tmp_y, num_x))  # 调用ex1.py中的函数nx(tmp_x, tmp_y, num_x)，计算并返回值
        j += 1

    return array_x, array_y  # 返回新生成列表array_x，array_y


if __name__ == "__main__":
    file = 'data/bassum.dat'
    out_x, out_y = main(file)  # 调用主函数，接收返回值
    draw(out_x, out_y)  # 调用函数draw(tmp_x, tmp_y)，作图

    if os.path.exists('out.dat'):  # 每次执行程序都新生成out.dat
        os.system('rm out.dat')

    for n in range(0, len(out_x)):
        with open('out.dat', 'a') as file:
            file.write(str(round(out_x[n], 3)) + '    ' + str(round(out_y[n], 3)) + '\n')  # 写入新生成数据
