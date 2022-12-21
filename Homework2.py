
# Задача 1: Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

# def inputNumbers(inputText):
#     is_Ok = True
#     while is_Ok:
#         try:
#             number = float(input(f'{inputText}'))
#             is_Ok = False
#         except ValueError:
#             print('Its not a number!')
#     return number

# def sumNums(num):
#     sum = 0
#     for i in str(num):
#         if i != '.':
#             sum += int(i)
#     return sum

# num = inputNumbers('Enter the number: ')

# print(f'The sum of digits -> {sumNums(num)}')

# Задача 2: Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# def inputNumbers(inputText):
#     is_Ok = True
#     while is_Ok:
#         try:
#             number = int(input(f'{inputText}'))
#             is_Ok = False
#         except ValueError:
#             print('Its not a integer!')
#     return number

# num = inputNumbers('Enter a number: ')
# sum = 1
# print(sum, end= ' ')
# for n in range(2, num + 1):
#     sum *= n 
#     print(sum, end= " ")  

# Задача 3: Задайте список из n чисел последовтельности (1+1/n)^n
# Выведите на экран их сумму.
#
# Пример:
# Для n= 4 {1: 2, 2:2.25, 3: 2.34, 4: 2.44}
# Сумма: 9,06

# Вариант 1:

# n = int(input('Enter a number: '))
# seq = [round((1 + 1/i) ** i, 2) for i in range(1, n + 1)]
# print(f'The sequence: {seq}\nAmount: {round(sum(seq), 2)}')

# Вариант 2 со словарями:

# n = int(input('Enter a number: '))
# seq = dict()
# seq_sum = 0
# for i in range(1, n+1):
#     seq[i] = round((1+1/i)**i, 2)
# print(f'For N = {n} {seq}')
# print(f'Amount: {sum(seq.values())}')

# Задача 4:Задайте список из N элементов, заполненных числами
# из промежутка [-N, N]. Найдите произведение элементов на
# указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# import random

# num = int(input("Ведите число: "))  # = 5
# my_list = []
# for i in range(num):
#     my_list.append(random.randint(-num, num))
# print(my_list)

# path = 'file.txt'
# data = open(path, 'w')
# data.write('2\n')
# data.write('4\n')
# data.close()

# path = 'file.txt'
# data = open(path, 'r')
# mult = 1
# for line in data:
#     mult*=my_list[int(line)]
# print(mult)

# Задача 5: Реализуйте алгоритм перемешивания списка.

import random

# Вариант 1:

# def list_shuffle(my_list: list):
#     shuffled_list = []
#     temp_list = my_list
#     print(temp_list)

#     for _ in range(len(my_list)):
#         position = random.randint(0, len(temp_list) - 1)
#         shuffled_list.append(temp_list.pop(position))
#     return shuffled_list


# print(list_shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

# Вариант 2:

my_list =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
orig_list = my_list
print(orig_list)
random.shuffle(my_list)
print(my_list)