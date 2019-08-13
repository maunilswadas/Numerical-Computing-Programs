def compute_float_epsilon():
    f_temp = 0.5
    while 1 + f_temp > 1:
        f_temp /= 2
    return f_temp


class Epsilon:
    float_epsilon = compute_float_epsilon()

    @classmethod
    def float_value(cls):
        return cls.float_epsilon
