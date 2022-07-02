from utils import *
import matplotlib.pyplot as plt


def get_sum(display=0):
    plt.figure(figsize=(9, 11))
    plt.subplots_adjust(hspace=0.5)

    plt.subplot(3, 1, 1)
    _x1, _y1 = get_data(data_dir.joinpath(file[0]))
    plt.title(file[0])
    plt.plot(_x1, _y1, 'black')

    plt.subplot(3, 1, 2)
    _x2, _y2 = get_data(data_dir.joinpath(file[1]))
    plt.title(file[1])
    plt.plot(_x2, _y2, 'black')

    plt.subplot(3, 1, 3)
    _x, _y = process_data_sum(_x1, [_y1, _y2])
    file_dir = out_dir.joinpath("sum.txt")
    write_file([_x, _y], file_dir)
    plt.title("sum")
    plt.plot(_x, _y, 'black')

    file_name = out_dir.joinpath("sum.pdf")
    plt.savefig(file_name, format="pdf")

    if display != 0:
        plt.show()
    else:
        plt.close()


def get_other(display=0):
    for i in range(0, 2):
        plt.figure(figsize=(9, 11))
        plt.subplots_adjust(hspace=0.5)

        plt.subplot(2, 1, 1)
        _x, _y = get_data(data_dir.joinpath(file[i]))
        plt.title(file[i])
        plt.plot(_x, _y, 'black')

        plt.subplot(2, 1, 2)
        plt.title(method[i])
        _x, _y = process_data_other(method[i], [_x, _y])
        file_dir = out_dir.joinpath(file[i].split(".")[0] + ".txt")
        write_file([_x, _y], file_dir)
        plt.plot(_x, _y, 'black')

        file_name = out_dir.joinpath(file[i].split(".")[0] + ".pdf")
        plt.savefig(file_name, format="pdf")

        if display != 0:
            plt.show()
        else:
            plt.close()


if __name__ == "__main__":
    data_dir = pathlib.Path("data")
    out_dir = pathlib.Path("out")
    file = ["1054.dat", "1055.dat"]
    method = ["forward", "backward"]

    if not pathlib.Path.exists(out_dir):
        pathlib.Path.mkdir(out_dir)

    get_sum(display=1)
    get_other(display=1)
