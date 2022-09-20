# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (600, 600)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

# x1 = 50
# x2 = 350
# for i in range(len(rainbow_colors)):
#     x1 += 10
#     x2 += 10
#     sd.line(sd.get_point(x1, 50), sd.get_point(x2, 350), color=rainbow_colors[i], width=4)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво


radius = 350
for color in rainbow_colors:
    radius += 25
    point = sd.get_point(300, -50)
    sd.circle(point, radius=radius, color=color, width=20)

sd.pause()
