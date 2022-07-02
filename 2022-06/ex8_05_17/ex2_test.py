from digitalSignal import darray, dfs

x = darray([range(0, 6), [1, 2, 4, 3, 0, 5]])

# print(dfs.dfs(x, n=10, k=0))
print(dfs.abs(x, k=range(-1, 5)))

x_n = [range(0, 11), [x(i) for i in range(0, 11)]]
x_n_dfs_abs = [range(0, 11), [dfs_abs(x_n, k) for k in range(0, 11)]]
