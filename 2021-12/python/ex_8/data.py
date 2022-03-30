import numpy as np
import os
import image


def main(k):
    for num in np.arange(0, 10, 0.1):
        file_name = 'data/f' + str(k) + '.txt'
        with open(file_name, 'a') as file:
            file.write(str(round(num, 2)) + '  ' + str(image.f(num, k)) + '\n')


if __name__ == "__main__":
    if not os.path.exists('data'):
        os.mkdir('data')
    for j in range(1, 4):
        main(j)
