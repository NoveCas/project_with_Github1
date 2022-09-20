# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
sd.resolution = (1000, 500)
point_x = 0
point_y = 0
brick_wight = 100
brick_height = 50
row_brick_number = 10
row_number = 10
red = [127, 0, 0]

for current_row in range(row_number):
    offset = 50 if current_row % 2 == 0 else 0
    for current_brick in range(row_brick_number):
        left_bottom_x = point_x + offset + brick_wight * current_brick
        left_bottom_y = point_y + brick_height * current_row
        left_bottom = sd.get_point(left_bottom_x, left_bottom_y)
        right_top_x = left_bottom_x + brick_wight
        right_top_y = left_bottom_y + brick_height
        right_top = sd.get_point(right_top_x, right_top_y)
        sd.rectangle(left_bottom, right_top, color=red, width=3)


sd.pause()
y2 = 0
number = 0
