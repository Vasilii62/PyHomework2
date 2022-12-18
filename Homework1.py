# Задача 1 Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет


# day = int(input('Enter the day of the week with the number: '))
# if 6 <= day <= 7:
#     print('Yes, its a holiday! ')
# elif 1 <= day <= 5:
#     print('No, its not a holiday!')
# else:
#     print('Enter the correct day of the week! ')

# Задача 2: Напишите программу для проверки истинности
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# for x in True, False:
#     for y in True, False:
#         for z in True, False:
#             print(f'x = {x} y = {y} z = {z}', end = ' ->')
#             print(not (x and y and z) == (not x) or (not y) or (not z))

# Задача 3: Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта
# точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = int(input('Enter coordinate x: '))
# y = int(input('Enter coordinate y: '))
# quarter = 0
# if x > 0 and y > 0:
#     quarter = 1
# elif x < 0 and y > 0:
#     quarter = 2
# elif x < 0 and y < 0:
#     quarter = 3      
# elif x > 0 and y < 0:
#     quarter = 4

# print(f'The quarter is -> {quarter}')

# Задача 4:Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y). 
    
# num_quarter = int(input('Enter the number of quarter: '))
# if num_quarter == 1:
#     print('X range from 0 to + ꚙ , Y range from 0 to + ꚙ')
# elif num_quarter == 2:
#     print('X range from 0 to - ꚙ , Y range from 0 to + ꚙ')
# elif num_quarter == 3:
#     print('X range from 0 to - ꚙ , Y range from 0 to - ꚙ')
# elif num_quarter == 4:
#     print('X range from 0 to + ꚙ , Y range from 0 to - ꚙ')
# else:
#     print('Sorry, but exist only 4 quarters!')

# Задача 5: Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math
x1 = int(input('Enter X of points A: '))
y1 = int(input('Enter Y of points A: '))
x2 = int(input('Enter X of points B: '))
y2 = int(input('Enter Y of points B: '))

print(round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 3))
