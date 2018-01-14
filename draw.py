import math
import turtle

import main


def draw_line(t1: turtle.Turtle, x1, y1, x2, y2):
    t1.penup()
    t1.goto(x1, y1)
    t1.pendown()
    t1.goto(x2, y2)


def draw_triangles(t1: turtle.Turtle):
    for i in range(0, 9):
        draw_line(t1, i * main.base, 0, (i + 0.5) * main.base, main.height)
        draw_line(t1, (i + 0.5) * main.base, main.height, (i + 1) * main.base, 0)


def start(t: turtle.Turtle, position, angle):
    if angle == math.pi / 2:
        draw_line(t, position, main.height, position, main.y(position))
    else:
        draw_line(t, position + 1 / math.tan(angle) * (main.height - main.y(position)), main.height, position,
                  main.y(position))
    index = 0
    while not math.isnan(position) and not math.isnan(angle):
        position, angle = main.exit_status(position, angle) if index % 2 == 0 else main.enter_status(position, angle)
        if not math.isnan(position) and not math.isnan(angle):
            t.goto(position + main.base * int((index + 1) / 2), main.y(position))
            index += 1
    return int(index / 2) + 1


ttl = turtle.Turtle()
ttl.hideturtle()
s = turtle.Screen()
s.screensize(2000, 2000)
ttl.speed(100)
draw_triangles(ttl)


def vary(get_x, get_angle, rng):
    for i in range(1, rng):
        ttl.color("#FFC107")
        params = (get_x(i, rng), get_angle(i, rng))
    # if params[1] < (math.pi - main.theta):
        entered_count = start(ttl, params[0], params[1])
        print(entered_count, params)
        ttl.color("black")
        ttl.write(i, font=("Arial", 16, "bold"))


vary(lambda x, y: main.base * 0.1, lambda x, y: math.pi / 2 + math.pi / 2 * x / y, 30)
s.exitonclick()
