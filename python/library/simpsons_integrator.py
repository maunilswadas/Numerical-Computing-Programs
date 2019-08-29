class SimpsonsIntegrator:

    def __init__(self, integrand):
        self.integrand = integrand

    def integrate(self, a, b, intervals):
        if b <= a:
            return 0

        h = (b - a)/intervals/2
        total_area = 0

        for i in range(intervals):
            x1 = a + 2*i*h
            total_area += self.area_of(x1, h)

        return total_area

    def area_of(self, x1, h):
        x2 = x1 + h
        x3 = x2 + h
        y1 = self.integrand.at(x1)
        y2 = self.integrand.at(x2)
        y3 = self.integrand.at(x3)
        area = h * (y1 + 4*y2 + y3) / 3
        return area
