#Домашнее задание

# Урок 5. Рекурсия и алгоритмы
# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# def stepen(b):
#     if b==1:
#         return a
#     return stepen(b-1)*a

# a=int(input("Введите число a"))
# b=int(input("Введите число b"))
# print('Число а в степени b, равно',stepen(b))

# _______________________________________________________
# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

# def sum(a,b):
#     if a==0:
#         return b
#     return sum(a-1, b+1)

# a=int(input("Введите число a"))
# b=int(input("Введите число b"))
# print('сумма двух целых неотрицательных чисел, равна',sum(a,b))