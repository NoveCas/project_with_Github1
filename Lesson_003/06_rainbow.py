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



for x in range(50, 121, 10):
    point_1 = sd.get_point(x,50)
    for x1 in range(350, 421, 10):
        point_2 = sd.get_point(x1,450)
        sd.line(point_1, point_2, width=5)


# for x1 in range(50, 351, 50):
#     for y1 in range(50, 351, 50):
#         for x2 in range(350, 701, 50):
#             for y2 in range(450, 801, 50):
#                 point_1 = sd.get_point(x1, y1)
#                 point_2 = sd.get_point(x2, y2)
#                 sd.line(point_1, point_2, width=4)



# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво


radius = 350
for color in rainbow_colors:
    radius += 25
    point = sd.get_point(300, -50)
    sd.circle(point, radius=radius, color=color, width=20)

sd.pause()
