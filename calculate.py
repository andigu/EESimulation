import math
import time

import main


def now():
    return int(round(time.time() * 1000))


def start(pos, angle, config):
    index = 0
    while not math.isnan(pos) and not math.isnan(angle):
        pos, angle = main.exit_status(pos, angle, config) if index % 2 == 0 else main.enter_status(pos, angle, config)
        if not math.isnan(pos) and not math.isnan(angle):
            index += 1
    return int(index / 2) + 1


def vary(get_x, get_angle, rng, config: main.Parameters):
    return sum(1 - ((1 - 0.04) ** start(get_x(j, rng), get_angle(j, rng), config)) for j in range(rng)) / rng


file = open('data.txt', 'w')
c = main.Parameters(100, 100, 1, 1.49)
t = now()
for i in range(1, 10000, 100):
    c.height = i
    print(i / 100, vary(lambda x, y: c.base * 0.1, lambda x, y: math.pi / 2 + math.pi / 2 * x / y, 900, c))
file.close()
print(now() - t)
