import pathlib
import subprocess


def get_data(_file_dir):
    """
    :param _file_dir: the directory of file
    :return: list: [x, y]
    """
    _x, _y = [[], []]
    _file_dir = pathlib.Path(_file_dir)

    if not pathlib.Path.exists(_file_dir):
        raise FileNotFoundError("{0} does not exist!".format(_file_dir))

    with open(_file_dir, "r") as _file:
        _lines = _file.readlines()

    for line in _lines:
        line = line.split("    ")
        _x.append(float(line[1].lstrip()))
        _y.append(float(line[2].lstrip().replace('\n', '')))

    return [_x, _y]


def process_data_sum(_x, _yy):
    """
    :param _x: list: x
    :param _yy: list: [y_1, y_2]
    :return: list: [x, y_new]
    """
    _y_new = []
    _y_1, _y_2 = _yy

    if len(_y_1) != len(_y_2):
        raise ValueError(
            "len(_y_1) = {0} and len(_y_2) = {1} is not equal!".format(len(_y_1), len(_y_2)))

    for k in range(0, len(_x)):
        _y_new.append(_y_1[k] + _y_2[k])

    return [_x, _y_new]


def process_data_other(_method, _xy):
    """
    :param _method: string: forward, backward
    :param _xy: list: [x, y]
    :return: list: [x_new, y_new]
    """
    _x, _y = _xy
    _x_new, _y_new = [_x, []]

    if len(_x) != len(_y):
        raise ValueError(
            "len(_x) = {0} and len(_y) = {1} is not equal!".format(len(_x), len(_y)))

    for n in _x:
        if _method == "forward":
            if not n + 1 in _x:
                _y_new.append(0.)
            else:
                _y_new.append(_y[_x.index(n + 1)] - _y[_x.index(n)])
        elif _method == "backward":
            if not n - 1 in _x:
                _y_new.append(0.)
            else:
                _y_new.append(_y[_x.index(n)] - _y[_x.index(n - 1)])

    return [_x_new, _y_new]


def write_file(_xy, _file_dir):
    """
    :param _xy: list: [x, y]
    :param _file_dir: the directory of file
    """
    _x, _y = _xy
    _file_dir = pathlib.Path(_file_dir)

    if pathlib.Path.exists(_file_dir):
        subprocess.run(['rm', _file_dir])

    with open(_file_dir, "a") as _file:
        for j in range(0, len(_x)):
            _file.write("{0:>12}".format(str("%.3f" % _x[j])))
            _file.write("{0:>12}".format(str("%.3f" % _y[j])))
            _file.write("\n")
