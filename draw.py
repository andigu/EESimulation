import math
import turtle

import main

config = main.defaultConfig


def draw_line(t1: turtle.Turtle, x1, y1, x2, y2):
    t1.penup()
    t1.goto(x1, y1)
    t1.pendown()
    t1.goto(x2, y2)


def draw_triangles(t1: turtle.Turtle):
    for i in range(0, 9):
        draw_line(t1, i * config.base, 0, (i + 0.5) * config.base, config.height)
        draw_line(t1, (i + 0.5) * config.base, config.height, (i + 1) * config.base, 0)


def start(t: turtle.Turtle, position, angle):
    if angle == math.pi / 2:
        draw_line(t, position, config.height, position, main.y(position))
    else:
        draw_line(t, position + 1 / math.tan(angle) * (config.height - main.y(position)), config.height, position,
                  main.y(position))
    index = 0
    while not math.isnan(position) and not math.isnan(angle):
        position, angle = main.exit_status(position, angle) if index % 2 == 0 else main.enter_status(position, angle)
        if not math.isnan(position) and not math.isnan(angle):
            t.goto(position + config.base * int((index + 1) / 2), main.y(position))
            index += 1
    return int(index / 2) + 1


ttl = turtle.Turtle()
ttl.hideturtle()
s = turtle.Screen()
s.screensize(2000, 2000)
ttl.speed(100)
draw_triangles(ttl)


def vary(get_x, get_angle, rng):
    for i in range(rng):
        ttl.color("#FFC107")
        params = (get_x(i, rng), get_angle(i, rng))
        entered_count = start(ttl, params[0], params[1])
        print(entered_count, params)
        ttl.color("black")
        # ttl.write(chr(i + 65), font=("Arial", 16, "bold"))


vary(lambda x, y: config.base/2 * x/y, lambda x, y: math.pi*0.75, 50)
s.exitonclick()
