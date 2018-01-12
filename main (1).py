import math

win_width, win_height, bg_color = 2000, 2000, 'black'


# A beam will exit the surface once its angle w.r.t the horizontal is less than math.atan2(-y, base-x)
# Since y = height/(base/2) * x, this is equivalent to math.atan2(-height/base*2x, base-x)

def snells(n1, theta1, n2):
    try:
        return math.asin(n1 / n2 * math.sin(theta1))
    except ValueError:
        return float('nan')


def y(x1):
    return height / base * 2 * x1


def entrance_coords(exit_angle: float, x1: float) -> list:
    """
    Finds x coordinate and entrance angle w.r.t horizontal in the triangle **BEFORE SNELL'S LAW** that a beam enters,
    once it exits another triangle at a given angle and x
    :param exit_angle: Angle w.r.t horizontal at which the beam exits the triangle
    :param x1: X coordinate in the triangle that it exits
    :return: X coordinate in the triangle that it enters
    """
    length = math.sqrt((base - x1) ** 2 + y(base - x1) ** 2)
    theta = math.atan2(height, base / 2)
    a, b = theta + exit_angle, math.pi - 2 * theta
    c = math.pi - a - b
    entrance_coord_length = length / math.sin(c) * math.sin(a)  # sine law
    total_side_length = math.sqrt((base / 2) ** 2 + height ** 2)
    ratio = entrance_coord_length / total_side_length  # similar triangles
    return [ratio * base / 2, c - theta + math.pi]


def exit_coords(entrance_angle: float, x1: float) -> list:
    """
    Finds x coordinate and exit angle w.r.t horizontal in the triangle that a beam exits, once it enters that triangle
    at a given angle and x
    :param entrance_angle: Angle w.r.t. horizontal that beam enters
    :param x1: x coordinate that it enters
    """
    theta = math.atan2(height, base / 2)
    entrance_angle_normal = math.pi / 2 - (entrance_angle - theta)  # entrance angle w.r.t normal at point of entry
    new_angle_normal = snells(1, entrance_angle_normal, n)  # angle the beam is refracted to w.r.t normal
    a = new_angle_normal + (math.pi / 2 - theta)  # angle the beam is refracted to w.r.t horizontal
    b = math.pi - theta
    c = math.pi - b - a
    c_len = base - x1 * 2  # length of the side opposite to angle c
    exit_coords_length = c_len / math.sin(c) * math.sin(a)
    print(math.degrees(a), math.degrees(b), math.degrees(c), c_len, exit_coords_length)
    total_side_length = math.sqrt((base / 2) ** 2 + height ** 2)
    ratio = exit_coords_length / total_side_length  # similar triangles
    exit_angle_normal = theta - c
    return [base - (ratio * base / 2), math.pi / 2 - snells(n, exit_angle_normal, 1) - theta]


def will_exit(theta, x1):
    return theta <= math.atan2(-height / base * 2 * x1, base - x1)


base, height, n = 40, 200, 1.49
normal = -(math.pi / 2 - math.atan2(height, base))  # angle that the normal of first side makes w.r.t horizontal
