#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Bro', 'Mother', 'Father']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Nikolay', 193],
    ['Vladimir', 187],
    ['Natali', 165]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Haight', my_family[2], my_family_height[1][1], 'cm')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
common_height = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1]

print('Common haight family - ', common_height, 'cm')