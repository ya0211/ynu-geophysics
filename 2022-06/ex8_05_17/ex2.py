from ex8_05_17.utils import dfs, dfs_abs, draw
import numpy as np


x = [range(0, 6), [1, 2, 4, 3, 0,  5]]

[print("X({0}): {1}".format(i, dfs(x, i))) for i in range(0, 6)]
print("sum(X(5)): {0}".format(sum([dfs(x, i) for i in range(0, 6)])))
print("sum(|X(5)|**2): {0}".format(sum([dfs_abs(x, i)**2 for i in range(0, 6)])))

x_dfs_abs = [np.arange(0, 6, 0.01), [dfs_abs(x, i) for i in np.arange(0, 6, 0.01)]]
draw(x_y=[x, x_dfs_abs],
     text=["x", "x_dfs_abs"],
     fig_size=(9, 12),
     style=["stem", "plot"],
     file_name="figure2.pdf")
