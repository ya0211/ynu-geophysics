from ex8_05_17.utils import convolution, draw
from ex7_05_03.utils import expand_r


x = [range(0, 5), [1, 0, 2, 1, 3]]

x_x = convolution(x=x, h=x)
x_5_x = convolution(x=x, h=expand_r(x, 5), ll=5)
x_10_x = convolution(x=x, h=expand_r(x, 10), ll=10)

draw(x_y=[x, x_x, x_5_x, x_10_x],
     text=["x", "x_x", "x_5_x", "x_10_x"],
     fig_size=(12, 9),
     style="stem",
     file_name="figure1.pdf")
