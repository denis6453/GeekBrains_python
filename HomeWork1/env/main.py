
import random
import math
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

def min_digit(digit_one, digit_two):
    if digit_one >= digit_two:
        min = digit_two
    else:
        min = digit_one
    return min  

count_monet = int(input("Введите количество монет: "))

monets_list = []

for i in range(0, count_monet):
    monets_list.append(random.choice([True, False]))

print(monets_list)

n_count = 0

for i in monets_list:
    if i:
        n_count = n_count + 1 

print(min(n_count, count_monet - n_count))    
     


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

##Petr
# number_x = random.randint(0, 1000)
# number_y = random.randint(0, 1000)
# print('Petr definition two digit ' + str(number_x) + ' and ' + str(number_y))

# numbers_summ = number_x + number_y
# numbers_p = number_x * number_y

# print('S = ' + str(numbers_summ) + ' P = ' + str(numbers_p))

# ##Kate
# discrement = math.sqrt(numbers_summ * numbers_summ - 4 * numbers_p)
# number_one = (numbers_summ + discrement)/2
# number_two = (numbers_summ - discrement)/2

# print('Kate definition two digit ' + str(int(number_one)) + ' and ' + str(int(number_two)))



# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# n = int(input("Введите N: "))


# exp = 0

# while n > 2 ** exp:
#     print (2 ** exp)
#     exp = exp + 1



# задача 1 сложная необязательная Посчитать сумму цифр любого целого или вещественного числа. Через строку решать нельзя.

# digit = 12345.12345

# while digit % 1 != 0:
#     digit *= 10

# def sum_digit (digit):
#     sum = 0
#     while (digit != 0):
#         sum = sum + digit % 10
#         digit = int(digit / 10)
#     return int(sum)

# print(sum_digit(digit))

# задача Де моргана необязательная
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# теперь надо проверить ее практически
# в цикле 100 раз прогоняем
# каждый раз генерируем случайное количество предикат от 3 до 15
# и конечно со случайным булевым значением
# и засекаем общее время выполнения программы
# юзаем библиотеки random и time
# предикаты НЕ ЗАДАЕМ как целое число!

# задача 3 необязательная

# Валентина прогуляла лекцию по математике.
# Преподаватель решил подшутить над нерадивой студенткой и
# попросил ее на практическом занятии перечислить все положительные делители некоторых целых чисел.
# Для несложных примеров студентка быстро нашла решения (для числа 6 это: 1, 2, 3, 6; а для числа 16 это: 1, 2, 4, 8, 16), но этим все не закончилось.
# На домашнее задание ей дали варианты посложнее: 23436, 190187200, 380457890232.

# Решить такое вручную, как вы понимаете, практически нереально.
# Вот Валентина и обратилась к вам за помощью.
# Помогите ей (при помощи функции all_divisors(number), которую напишете сами).
# Постарайтесь найти самое оптимальное решение.
# Результат представьте в виде списка (не забудьте отсортировать по возрастанию).

# def all_divisors (number):
#     divisors = []
#     for i in range (1, int(number ** 0.5) + 1):
#         if number % i == 0:
#             divisors.append(i)
#             divisors.append(number // i)
#     return sorted(set(divisors))

# print (all_divisors(380457890232))