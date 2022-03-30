import numpy as np
import interpolation
import image


file_name = 'data/decdata.dat'
array_x, array_y = image.get_data(file_name)

data_x, data_y, j = [[], [], 0]
for u in np.arange(-5.040, 40.0, 0.4):
    yu = interpolation.main(u, array_x, array_y)
    interpolation.add(u, yu, j, data_x, data_y, array_x, array_y)
    j += 1

interpolation.draw(data_x, data_y)
