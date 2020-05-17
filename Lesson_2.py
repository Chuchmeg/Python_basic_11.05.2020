#Первое задание

var_list = [1, 2, 'Привет', True, 0.1, (2,3,23445), {4,5,6}]
for list_type in var_list:
    print (type(list_type))
print('-----------------------------------------------------------------------------------')

#Второе задание

input_list = input('Введи все, что душе угодно\n')
input_list = list(input_list)
el = 0
# input_list = list(input_list)
for elem in range(len(input_list) // 2):
    input_list[el], input_list[el + 1] = input_list[el + 1], input_list[el]
    el +=2

print(''.join(input_list))
print('-----------------------------------------------------------------------------------')
#Третье задание

seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
input_month = input('Введите номер месяца\n')
if input_month.isdigit():
    input_month = int(input_month)
    if 1 <= input_month <= 2 or input_month == 12:
        print('dict: ', seasons_dict.get(1))
        print('list: ', seasons_list[0])
    elif 3 <= input_month <= 5:
        print('dict: ', seasons_dict.get(2))
        print('list: ', seasons_list[1])
    elif 6 <= input_month <= 8:
        print('dict: ', seasons_dict.get(3))
        print('list: ', seasons_list[2])

    elif 9 <= input_month <= 11:
        print('dict: ', seasons_dict.get(4))
        print('list: ', seasons_list[3])
    else:
        print('Нет такого месяца вообще-то')
else:
    print('Ну введи ты циферку, ну!')
print('-----------------------------------------------------------------------------------')
#Четвертое задание

input_string = input("Введи предлождение \n")
counter = 1
for el in range(input_string.count(' ') + 1):
    split_string = input_string.split()
    if len(str(split_string)) <= 10:
        print(f" {counter} {split_string [el]}")
        counter += 1
    else:
        print(f" {counter} {split_string [el] [0:10]}")
        counter += 1
print('-----------------------------------------------------------------------------------')

#Пятое задание

rating_list = [8,6,4,3,3,2]
print(rating_list)
input_rating = input('Введите число \n')
if input_rating.isdigit():
    input_rating = int(input_rating)
    for el in range(len(rating_list)):
        if rating_list[el] == input_rating:
            rating_list.insert(el + 1, input_rating)
            break
        elif rating_list[0] < input_rating:
            rating_list.insert(0, input_rating)
            break
        elif rating_list[-1] > input_rating:
            rating_list.append(input_rating)
            break
        elif rating_list[el] > input_rating > rating_list[el + 1]:
            rating_list.insert(el + 1, input_rating)
            break
    print(rating_list)
else:
    print('Ну введи ты циферку, ну!')