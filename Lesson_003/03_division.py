# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 179, 37

# TODO здесь ваш код
int_divisor = 0
multiplication = 0
while multiplication <= a:
    int_divisor += 1
    multiplication = b * int_divisor

int_divisor -= 1
print('Целочисленное деление {} на {} дает {}'.format(a,b,int_divisor))