# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(300, 300)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг

def bubble(point, step):
    radius = 50
    a = random.randint(1, 255)
    b = random.randint(1, 255)
    c = random.randint(1, 255)
    random_color = [a, b, c]
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=random_color, width=2)


# Нарисовать 10 пузырьков в ряд

# Нарисовать три ряда по 10 пузырьков
# for y in range(100, 301,100):
#     for x in range(100, 1100, 100):
#         point = sd.get_point(x, y)
#         bubble(point=point, step=5)


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 10)
    bubble(point=point, step=step)

sd.pause()


