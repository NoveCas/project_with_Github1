# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = int(input("Введите, пожалуйста, номер месяца: "))



month = [
    ['January', 1, 31], ['February', 2, 28], ['March', 3, 31],
    ['April', 4, 30], ['May', 5, 31], ['June', 6, 30],
    ['Jule', 7, 31], ['August', 8, 31],['September', 9, 30],
    ['October', 10, 31], ['November', 11, 30], ['December', 12, 31]
]

if user_input == month[0][1]:
    print('This month has', month[0][2], 'days.')
elif user_input == month[1][1]:
    print('This month has', month[1][2], 'days.')
elif user_input == month[2][1]:
    print('This month has', month[2][2], 'days.')
elif user_input == month[3][1]:
    print('This month has', month[3][2], 'days.')
elif user_input == month[4][1]:
    print('This month has', month[4][2], 'days.')
elif user_input == month[5][1]:
    print('This month has', month[5][2], 'days.')
elif user_input == month[6][1]:
    print('This month has', month[6][2], 'days.')
elif user_input == month[7][1]:
    print('This month has', month[7][2], 'days.')
elif user_input == month[8][1]:
    print('This month has', month[8][2], 'days.')
elif user_input == month[9][1]:
    print('This month has', month[9][2], 'days.')
elif user_input == month[10][1]:
    print('This month has', month[10][2], 'days.')
elif user_input == month[11][1]:
    print('This month has', month[11][2], 'days.')
else:
    print('This month dosnt exist')


#THERE I TRIED TO REALIZE CYCLE FOR...
# for month_fact in month:
#     for days in month_fact:
#         if isinstance(days,str):
#             continue
#         elif user_input == days:
#             print(month[0][2])
#         elif days == 2:
#             print(month[1][2])
#         elif days == 3:
#             print(month[2][2])
#         elif days == 4:
#             print(month[3][2])
#         elif days == 5:
#             print(month[4][2])
#         elif days == 6:
#             print(month[5][2])
#         elif days == 7:
#             print(month[6][2])
#         elif days == 8:
#             print(month[7][2])
#         elif days == 9:
#             print(month[8][2])
#         elif days == 10:
#             print(month[9][2])
#         elif days == 11:
#             print(month[10][2])
#         elif days == 12:
#             print(month[11][2])
#         else:
#             print('Вы ввели неккоректынй номер')
#

