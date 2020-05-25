#Первое задание

from sys import argv

name, time, salary, bonus = argv
try:
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    res = time * salary + bonus
    print(f'заработная плата сотрудника  {res}')
except ValueError:
    print('Not a number')

#Второе задание

my_list = [36, 43, 4, 132, 34, 567, 12, 1233, 88, 95]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')
print(f'Числа от 20 до 240 кратные 20 или 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

#Третье задание

my_list_1 = [3, 2, 4, 5, 5, 9, 4, 5, 3, 1]
my_new_list_1 = [el for el in my_list_1 if my_list_1.count(el) < 2]
print(my_new_list_1)

#Четвертое задание

from functools import reduce
def my_func(el_prev, el):
    return el_prev * el
print(f'Список четных значений {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения всех элементов списка {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')

#Пятое задание

from itertools import count
for el in count(int(input('Введите стартовое число '))):
    if el > 10000:
        break
    print(el)

from itertools import cycle
c_2 = 0
my_list_2 = [1, 123, 'Привет']
for el in cycle(my_list_2):
    if c_2 > 10:
        break
    print(el)
    c_2 += 1

#Шестое задание

from itertools import count
from math import factorial

def fact():
    for el in count(1):
        yield factorial(el)

gen = fact()
a = 0
for i in gen:
    if a < 10:
        print(i)
        a += 1
    else:
        break