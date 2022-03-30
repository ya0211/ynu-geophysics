import numpy as np
import os
import interpolation
import image

file_name = 'data/decdata.dat'
array_x, array_y = image.get_data(file_name)

dt = 0.4
if os.path.exists('out.dat'):
    os.system('rm out.dat')
for value in [-4.84, -4.94]:
    data_x, data_y, j = [[], [], 0]
    for u in np.arange(value, 40.0, dt):
        yu = interpolation.main(u, array_x, array_y)
        interpolation.add(u, yu, j, data_x, data_y, array_x, array_y)
        j += 1
    dt = dt - 0.2
    array_x, array_y = data_x, data_y

interpolation.draw(data_x, data_y)
