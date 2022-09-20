# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код

# point_1 = sd.get_point(0,0)      #(100, 0)
# point_2 = sd.get_point(100, 0)   #(200, 0)
# point_3 = sd.get_point(100, 50)  #(200, 50)
# point_4 = sd.get_point(0, 50)    #(100,50)

x1 = 0
x2 = 100
for x in range(10):
    point_1 = sd.get_point(x1, 0)
    point_2 = sd.get_point(x2, 0)
    point_3 = sd.get_point(x2, 50)
    point_4 = sd.get_point(x1, 50)
    for x1 in range(1):
        x1 += 100
        x2 += 100
        sd.line(point_1, point_2, width=1)
        sd.line(point_2, point_3, width=1)
        sd.line(point_3, point_4, width=1)
        sd.line(point_4, point_1, width=1)



sd.pause()
