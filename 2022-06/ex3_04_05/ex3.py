import pathlib
import matplotlib.pyplot as plt
from ex2_03_29.utils import multipy_then_add


def draw(_x, _y, file_name, display=0):
    plt.figure(figsize=(9, 11))
    plt.subplots_adjust(hspace=0.5)

    for _i in range(0, len(_x)):
        plt.subplot(3, 1, _i+1)
        plt.title("x = {0}".format(_y[_i]))
        plt.plot(_x[_i], _y[_i], 'black')

    file_name = out_dir.joinpath(file_name)
    plt.savefig(file_name, format="pdf")

    if display != 0:
        plt.show()
    else:
        plt.close()


def main(_x, _x_index, _y, _y_index):
    _m, _tmp_list = [[], []]
    for _i in range(-(_y_index[-1]-_x_index[0]), _x_index[-1]-_y_index[0]+1):
        _m.append(_i)
    for _j in range(-1, -len(_y)-1, -1):
        _tmp_list.append(_y[_j])

    _mta = multipy_then_add(_x, _tmp_list)
    # print("x: {0}".format(_mta.get('x')))
    # print("y: {0}".format(_mta.get('y')))
    # print("tmp list: {0}".format(_mta.get('t')))

    return _m, _mta.get('r')


if __name__ == "__main__":
    out_dir = pathlib.Path("out")

    if not pathlib.Path.exists(out_dir):
        pathlib.Path.mkdir(out_dir)

    x = [5, 4, 3, 2, 1]
    x_index = range(0, 5)
    y = [2, 4, 6]
    y_index = range(0, 3)

    m, r_xy = main(x, x_index, y, y_index)
    print("m: {0}".format(m))
    print("r_xy: {0} \n".format(r_xy))
    draw([x_index, y_index, m], [x, y, r_xy], "other.pdf", display=0)

    m, r_xx = main(x, x_index, x, x_index)
    print("m: {0}".format(m))
    print("r_xx: {0}".format(r_xx))
    draw([x_index, m], [x, r_xx], "self.pdf", display=0)

    """
    5, 4, 3, 2, 1
          6, 4, 2

            10, 08, 06, 04, 02
        20, 16, 12, 08, 04
    30, 24, 18, 12, 06

    30, 44, 44, 32, 20, 08, 02

    5, 4, 3, 2, 1
    1, 2, 3, 4, 5

                    25, 20, 15, 10, 05
                20, 16, 12, 08, 04
            15, 12, 09, 06, 03
        10, 08, 06, 04, 02
    05, 04, 03, 02, 01

    05, 14, 26, 40, 55, 40, 26, 14, 05

    """
