# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

month = 10
month_cicle = 0
money_parents = 0
educational_grant_cicle = 0
expenses_cicle = 0
while month_cicle < month:
    month_cicle += 1
    money_parents += expenses - educational_grant
    educational_grant_cicle += educational_grant
    expenses_cicle = expenses * 3 / 100
    expenses += expenses_cicle
money_parents = round(money_parents,2)
print('Cтуденту надо попросить {} рублей'.format(money_parents))
