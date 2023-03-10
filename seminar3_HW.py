#Домашнее задание

#Семинар 3

# Найти количество вхождений

# Вам дан список list_1, состоящий из целых чисел. Длина списка не превышает 100 элементов. А также целое число k.
# Найдите количество вхождений числа k в список list_1. Результат запишите в переменную res. Выводить переменную res на экран не требуется.

# Пример:
# Дано: list_1 = [1, 2, 3, 3, 4, 5]
# k = 3
# Результат: res = 2

# list_1 = [1, 2, 3, 3, 3, 4, 5]
# k=3
# res=0
# while k in list_1:
#     list_1.remove(k)
#     res=res+1
# print(res)

# ___________________________________________________

# Ближайший элемент
# Вам даны число k и список list_1, состоящий из целых чисел. Длина списка не превышает 100 элементов. 
# Число k удовлетворяет условию -100 >= k <= 100.

# Найдите в list_1 ближайший по величине к числу k элемент. Сохраните этот элемент в переменную res. 
# Выводить переменную res на экран не требуется.
# Примечание: Ближайший по величине элемент определяется следующим оборазом: 
# рассчитывается абсолютная разница между каждым элементом list_1 и k, 
# а затем берется элемент списка с минимальной абсолютной разницей.

# Если в списке list_1 несколько элементов одинаково близки по величине к k - в переменную res запишите число, 
# идущее в списке первым.

# Пример:

# Дано: list_1 = [1, 2, 3, 3, 4, 6]
# k = 10
# Результат: res = 6

# Дано: list_1 = [1, 2, 3, 3, 4, 6]
# k = 5
# Результат: res = 4

# Дано: list_1 = [1, 2, 3, 3, 4, 6]
# k = 3
# Результат: res = 3

# list_1 = [1, 2, 3, 3, 4, 6]
# k=5
# min=200
# res=0
# i=0
# ind=0
# while i in range(len(list_1)):
#     res=abs(list_1[int(i)]-k)
#     if res<min:
#         min=res
#         ind=list_1[int(i)]
#     i=i+1
# print(ind)
# _________________________________________________________

#Скрабл

# Пролог
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:

# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:

# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Дано
# Вам дана переменная word, которая содержит слово только из английских, либо только из русских букв.

# Задание
# Напишите программу, которая вычисляет стоимость данного слова. Результат - число - запишите в переменную res. Выводить переменную res на экран не требуется.

# Пример:

# Дано: word = 'sun'
# Результат: res = 3

# word = input('введите слово')
# points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JZ', 10: 'QZ'}
# points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
# word = word.upper()  
# res = 0
# for i in word:
#     if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#         for j in points_en:
#             if i in points_en[j]:
#                 res = res + j
#     else:
#         for j in points_en:
#             if i in points_ru[j]:
#                 res = res + j
# print(res)