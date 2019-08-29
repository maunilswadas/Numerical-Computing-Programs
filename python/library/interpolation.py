import numpy as np


class InterpolationPolynomial:

    def __init__(self, max_points):
        self.pts_x = None
        self.pts_y = None
        self.num_pts = 0
        self.dd = np.empty((max_points, max_points))

    def set_data(self, data):
        self.pts_x = data['x']
        self.pts_y = data['y']
        self.num_pts = len(self.pts_x)
        self.calc_dd()

    def calc_dd(self):
        for n in range(self.num_pts):
            self.dd[n, 0] = self.pts_y[n]
            for order in range(1, n + 1):
                bottom = n - order
                numerator = self.dd[bottom + 1, order - 1] - self.dd[
                    bottom, order - 1]
                denominator = self.pts_x[bottom + order] - self.pts_x[bottom]
                self.dd[bottom, order] = numerator / denominator

    def at(self, x):
        y = self.dd[0, 0]
        x_factor = 1
        for order in range(1, self.num_pts):
            x_factor *= x - self.pts_x[order - 1]
            y += x_factor * self.dd[0, order]
        return y

    def pixel_data(self, width, x_min, x_max):
        x_delta = (x_max - x_min) / width
        line_x = [x_min + w * x_delta for w in range(width)]
        line_y = [self.at(x) for x in line_x]
        return dict(xs=[line_x], ys=[line_y])
