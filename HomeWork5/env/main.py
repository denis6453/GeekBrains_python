# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


# a1 = int(input("Введите первый элемент прогрессии: "))
# d = int(input("Введите разность прогрессии: "))
# n = int(input("Введите количество элементов прогрессии: "))

# def generate_progression (a1, d, n):
#     progression = []
#     for i in range(n):
#         progression.append(a1 + i * d)
#     return progression

# print("Элементы прогрессии:", generate_progression(a1,d,n))

# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума). 
# Список можно задавать рандомно

# import random

# def generate_list (n, a, b):
#     lst = [random.randint(a, b) for i in range(n)]
#     return lst

# def f (min_val, max_val, lst):
#     indexes = [ i for i in range(len(lst)) if min_val <= lst[i] <= max_val]
#     return indexes



# n = 10 
# a = -5 
# b = 5 
# min_val = -3 
# max_val = 3 

# lst = generate_list(n, a, b)
# print("Список:", lst)


# print(f(min_val, max_val, lst))



# Крестики нолики

def print_field (field_list):
    for i in range(len(field_list)):
        print (field_list[i])

def end_play (winner):
    if winner:
        print ("Поздравляем вы выиграли!!")
    else:
        print("Вы проиграли(")

def start_window():
    marker_player = input ("Введите символ за который вы будете играть: ")
    return marker_player

def step_info_player ():
    i = int(input ("Введите строку: "))
    j = int(input ("Введите столбец: "))
    # if i >= 0 and i <= 2 and j >= 0 and j <= 2:
    return i, j
    # else:
    #     print ("Вы ввели несуществующую позицию")
    #     step_info()

def step_info_bot (field_list):
    print ("Ходит бот!!!")
    for i in range(len(field_list)):
        for j in range(len(field_list[i])):
            if field_list[i][j] == ' ':
                return i,j
    # i = int(input ("Ходит бот. Введите строку: "))
    # j = int(input ("Ходит бот. Введите столбец: "))
    # if i >= 0 and i <= 2 and j >= 0 and j <= 2:
    return i, j
    # else:
    #     print ("Вы ввели несуществующую позицию")
    #     step_info()

def play_start (field_list, marker_player, marker_bot):
    while chek_end_play(field_list):
        i, j = step_info_player()
        field_list[i][j] = marker_player
        print_field(field_list)
        if chek_end_play(field_list):
            i, j = step_info_bot(field_list)
            field_list[i][j] = marker_bot
            print_field(field_list)
        else:
            break
    end_play(True)



def chek_end_play (field_list):
    # for i in range(len(field_list)):
    #     for j in range(len(field_list[i])):
    #         if field_list[i][j] == ' ':
    #             return True
    if chek_vertical(field_list) and chek_gorizontal(field_list) and chek_main_diag(field_list) and chek_side_diag(field_list):
        return True
    return False

def chek_vertical (field_list):
    for i in range(len(field_list)):
        if field_list[i][0] == field_list[i][1] == field_list[i][2] and field_list[i][0] != ' ':
            return False
    return True

def chek_gorizontal (field_list):
    for i in range(len(field_list)):
        for j in range(len(field_list[i])):
            if field_list[0][j] == field_list[1][j] == field_list[2][j] and field_list[0][j] != ' ':
                return False
    return True

def chek_main_diag (field_list):
    if field_list[0][0] == field_list[1][1] == field_list[2][2] and field_list[0][0] != ' ':
        return False
    return True

def chek_side_diag (field_list):
    if field_list[0][2] == field_list[1][1] == field_list[2][0] and field_list[0][2] != ' ':
        return False
    return True

field_list = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

print_field(field_list)

marker_player = start_window()

if marker_player != 'o':
    marker_bot = 'o'
else:
    marker_bot = 'x'

play_start(field_list, marker_player, marker_bot)
