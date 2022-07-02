import numpy as np


class FourierTransform:
    def __init__(self, a: list, n: int):
        self._a = a
        self._n = n

    def dfs(self, k: int):
        re = 0
        for index in range(0, self._n):
            re += self._a[index] * np.cos(2 * np.pi * index * k / self._n)

        im = 0
        for index in range(0, self._n):
            im -= self._a[index] * np.sin(2 * np.pi * index * k / self._n)

        return re, im

    def dfs_abs(self, k: int):
        re, im = self.dfs(k)
        return np.sqrt(re ** 2 + im ** 2)

    def dfs_arg(self, k: int):
        re, im = self.dfs(k)
        if re <= 10**(-15):
            """
            The real part is 0 and the argument cannot be calculated, return 0
            """
            return 0
        else:
            return np.arctan(im/re)
