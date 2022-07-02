def multipy_then_add(_x: list, _y: list):
    """
    :param _x: list: x
    :param _y: list: y
    :return: list: result
    """
    result, _tmp_list = [[], []]
    if len(_x) >= len(_y):
        multiplier_be, multiplier_af = _x, _y
    else:
        multiplier_be, multiplier_af = _y, _x

    for _index in range(-1, -len(multiplier_af)-1, -1):
        _list_multipy = []
        _count_be = len(multiplier_af) + _index
        _count_af = len(multiplier_af) - _count_be - 1

        if _count_be != 0:
            for _ in range(0, _count_be):
                _list_multipy.append(0)

        for _n in multiplier_be:
            _list_multipy.append(_n * multiplier_af[_index])

        if _count_af != 0:
            for _ in range(0, _count_af):
                _list_multipy.append(0)

        _tmp_list.append(_list_multipy)

    for _index_list in range(0, len(_tmp_list[0])):
        _sum = 0
        for _index_tmp in range(0, len(_tmp_list)):
            _sum = _sum + _tmp_list[_index_tmp][_index_list]
        result.append(_sum)

    return {'r': result, 'x': _x, 'y': _y, 't': _tmp_list}

