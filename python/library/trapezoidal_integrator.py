class TrapezoidalIntegrator:

    def __init__(self, integrand):
        self.integrand = integrand

    def integrate(self, a, b, intervals):
        if b <= a:
            return 0

        h = (b - a)/intervals
        total_area = 0

        for i in range(intervals):
            x1 = a + i*h
            total_area += self.area_of(x1, h)

        return total_area

    def area_of(self, x1, h):
        x2 = x1 + h
        y1 = self.integrand.at(x1)
        y2 = self.integrand.at(x2)
        area = h*(y1 + y2)/2
        return area
