#Домашнее задание

# Урок 6. Повторение списков
# Задача 30: Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# # Каждое число вводится с новой строки.


# n=int(input('введите количество элементов массива'))
# a1=int(input('введите первый элемент массива'))
# d=int(input('введите разность массива'))
# for i in range(n):
#     print(a1 + i * d)

# _______________________________________________________
# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и 
# не больше заданного максимума)


# n=int(input('введите количество элементов массива'))
# list1=list()
# import random
# for i in range(n):
#     list1.append(random.randint(-10,10))
# print(list1)
# minimum = int(input('введите значение минимума'))
# maximum = int(input('введите значение максимума'))
# for i in range(len(list1)):
#     if minimum<= list1[i]<=maximum:
#         print(i)