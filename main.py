import math


def snell(n1, theta1, n2):
    try:
        return math.asin(n1 / n2 * math.sin(theta1))
    except ValueError:
        return float('nan')


def y(x):
    return height / base * 2 * x if x < base / 2 else height / base * 2 * (base - x)


def length(a, b):
    return math.sqrt(a ** 2 + b ** 2)


def exit_status(enter_x, enter_angle):
    s = snell(n_air, math.pi / 2 - enter_angle + theta, n_acrylic)
    a, b = math.pi / 2 - theta + s, math.pi - theta
    c = math.pi - a - b
    l1 = (base - 2 * enter_x) / math.sin(c) * math.sin(a) + length(base/2 - enter_x, height - y(enter_x))
    print((base - 2 * enter_x) / math.sin(c) * math.sin(a), length(base/2 - enter_x, height - y(enter_x)), L)
    ratio = (L - l1)/L
    print(base - ratio * base/2)
    return base - ratio * base/2, theta - s - math.pi / 2


def enter_status(exit_x, exit_angle):
    s = snell(n_acrylic, math.pi * 3 / 2 - exit_angle - theta, n_air)
    a, c = math.pi / 2 - s, math.pi - 2 * theta
    b = math.pi - a - c
    l1 = length(base - exit_x, y(exit_x)) / math.sin(b) * math.sin(a)
    ratio = l1 / L
    return ratio * base / 2, math.pi / 2 - theta - s


# height = 200, 400 works well
base, height, n_air, n_acrylic = 100, 200, 1, 1.49
theta = math.atan2(height, base / 2)
L = length(base / 2, height)
