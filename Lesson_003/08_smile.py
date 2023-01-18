# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код
def smile_draw(x, y):
    point_smile = sd.get_point(x, y)
    color = sd.random_color()
    sd.circle(center_position=point_smile, radius=50, color=color, width=3)

    point_eye_1 = sd.get_point(x - 15, y + 15)
    sd.circle(center_position=point_eye_1, radius=5, color=color, width=1)

    point_eye_2 = sd.get_point(x + 15, y + 15)
    sd.circle(center_position=point_eye_2, radius=5, color=color, width=1)

    p1 = sd.get_point(x - 30, y - 10)
    p2 = sd.get_point(x - 5, y - 25)
    p3 = sd.get_point(x + 5, y - 25)
    p4 = sd.get_point(x + 30, y - 10)
    point_list = [p1, p2, p3, p4]
    sd.lines(point_list, color, width=1)

for _ in range(10):
    x1 = sd.random_point()
    y1 = sd.random_point()
    smile_draw(x1, y1)






sd.pause()
