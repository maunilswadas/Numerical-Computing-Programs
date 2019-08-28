import numpy as np


class RegressionLine:

    def __init__(self):
        self.sum_x = 0
        self.sum_y = 0
        self.sum_xx = 0
        self.sum_xy = 0
        self.a0 = 0
        self.a1 = 0
        self.n = 0

    def set_data(self, data):
        np_arr_x = np.array(data['x'])
        np_arr_y = np.array(data['y'])
        self.n = len(np_arr_x)

        self.sum_x = np_arr_x.sum()
        self.sum_y = np_arr_y.sum()
        self.sum_xx = (np_arr_x * np_arr_x).sum()
        self.sum_xy = (np_arr_x * np_arr_y).sum()
        x_bar = self.sum_x / self.n
        y_bar = self.sum_y / self.n
        self.a1 = (self.n * self.sum_xy - self.sum_x * self.sum_y) / (
                    self.n * self.sum_xx - self.sum_x * self.sum_x)
        self.a0 = y_bar - self.a1 * x_bar

    def at(self, x):
        return self.a0 + self.a1 * x

    def pixel_data(self, width, x_min, x_max):
        x_delta = (x_max - x_min) / width
        line_x = [x_min + w * x_delta for w in range(width)]
        line_y = [self.at(x) for x in line_x]
        return dict(xs=[line_x], ys=[line_y])
