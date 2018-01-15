import math


class Parameters:
    def __init__(self, base, height, n_air, n_acrylic):
        self.base = base
        self.height = height
        self.n_air = n_air
        self.n_acrylic = n_acrylic

    @property
    def theta(self):
        return math.atan2(self.height, self.base / 2)

    @property
    def length(self):
        return length(self.base / 2, self.height)


defaultConfig = Parameters(60, 300, 1, 1.49)


def snell(n1, theta1, n2):
    try:
        return math.asin(n1 / n2 * math.sin(theta1))
    except ValueError:
        return float('nan')


def y(x, config=defaultConfig):
    return config.height / config.base * 2 * x if x < config.base / 2 else config.height / config.base * 2 * (
            config.base - x)


def length(a, b):
    return math.sqrt(a ** 2 + b ** 2)


def exit_status(enter_x, enter_angle, config=defaultConfig):
    s = snell(config.n_air, math.pi / 2 - enter_angle + config.theta, config.n_acrylic)
    a, b = math.pi / 2 - config.theta + s, math.pi - config.theta
    c = math.pi - a - b
    l1 = (config.base - 2 * enter_x) / math.sin(c) * math.sin(a) + length(config.base / 2 - enter_x, config.height - y(enter_x))
    ratio = (config.length - l1) / config.length
    return config.base - ratio * config.base / 2, config.theta - s - math.pi / 2


def enter_status(exit_x, exit_angle, config=defaultConfig):
    s = snell(config.n_acrylic, math.pi * 3 / 2 - exit_angle - config.theta, config.n_air)
    a, c = math.pi / 2 - s, math.pi - 2 * config.theta
    b = math.pi - a - c
    l1 = length(config.base - exit_x, y(exit_x)) / math.sin(b) * math.sin(a)
    ratio = l1 / config.length
    return ratio * config.base / 2, math.pi / 2 - config.theta - s
