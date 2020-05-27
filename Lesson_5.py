#Первое задание

file_1 = open('test_1.txt', 'w')
input_text = input('Введи все что угодно \n')
while input_text:
    file_1.writelines(input_text + ' ')
    input_text = input('Еще давай херачь \n')
    if not input_text:
        break
file_1.close()
file_1 = open('test_1.txt', 'r')
content_1 = file_1.readlines()
print(content_1)
file_1.close()

#Второе задание

file_2 = open('test_2.txt', 'r')
content_2 = file_2.read()
print(f'Вот что там написано: \n {content_2}')
file_2 = open('test_2.txt', 'r')
content_2 = file_2.readlines()
print(f'Строк тут: {len(content_2)}')
file_2 = open('test_2.txt', 'r')
content_2 = file_2.readlines()
for i in range(len(content_2)):
    print(f'Количество слов в {i + 1} - ой строке: {len(content_2[i].split())}')
file_2.close()

#Третье задание

with open('test_3.txt', 'r') as file_3:
    salary = []
    workers = []
    my_list = file_3.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           workers.append(i[0])
        salary.append(i[1])
print(f'Оклад меньше 20.000 у: {", ".join(workers)}. А средний оклад {sum(map(int, salary)) / len(salary)}')

#Четвертое задание

rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('test_4_in.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
with open('test_4_out.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)

#Пятое задание

def summ():
    try:
        with open('test_5.txt', 'w+') as file_obj:
            line = input('Веди циффарки \n')
            file_obj.writelines(line)
            number= line.split()

            print(sum(map(int, number)))
    except IOError:
        print('Ошибка')
    except ValueError:
        print('Ошибка ввода')
summ()

#Шестое задание

subj = {}
with open('test_6.txt', 'r') as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')

#Седьмое задание

import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('test_7.txt', 'r') as file:
    for line in file:
        name, form, earned, spent = line.split()
        profit[name] = int(earned) - int(spent)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Средняя прибыль: {prof_aver:.2f}')
    else:
        print(f'Это фиаско, братан')
    pr = {'Average profit': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')
with open('test_7.json', 'w') as write_js:
    json.dump(profit, write_js)
    js_str = json.dumps(profit)
    print(f'Лови json файл: \n {js_str}')