#Первое задание
name = input('Ваше имя?\n')
age = input('Ваш возраст?\n')
if age.isdigit():
    print('Привет,', name)
    print('Тебе аж целых' ,age ,'годиков!')
else:
    print('Чувак, ну возраст то в циферках надо указывать!')

#Второе задание
input_time = input('Введи количество секунд, которое ты потом увидишь в формате чч:мм:сс, это ОЧЕНЬ надо:)\n')

if input_time.isdigit():
    input_time = int(input_time)
    hours = input_time // 3600
    minutes = (input_time - hours * 3600) // 60
    seconds = input_time - hours * 3600 - minutes * 60
    time_result = '{0}:{1}:{2}'.format(hours, minutes, seconds)
    print('А вот и результат: ', time_result)
else:
    print('Чота ты не то вводишь, братишь! В след раз введи ЦЫФФАРКИ!')

#Третье задание
n_number = input('Введи число \n')
if n_number.isdigit():
    n_number = int(n_number)
    n_number2 = n_number * 11
    n_number3 = n_number * 111
    print('Вот что в итоге вычисляем: ', n_number, '+', n_number2, '+', n_number3)
    n_result = n_number + n_number2 + n_number3
    print('Ваш результат: ', n_result)
else:
    print('Чота ты не то вводишь, братишь! В след раз введи ЦЫФФАРКИ!')
#Четвертое задание
pos_number = input('Введи ПОЛОЖИТЕЛЬНОЕ число \n')
if pos_number.isdigit():
    pos_number = int(pos_number)
    highest_number = pos_number % 10
    pos_number = pos_number // 10
    while pos_number > 0:
        if pos_number % 10 > highest_number:
            highest_number = pos_number % 10
        pos_number = pos_number // 10
    print('Вот и самая большая цифра: ', highest_number)
else:
    print('Чота ты не то вводишь, братишь! В след раз введи ЦЫФФАРКИ!')
#Пятое задание
rev_input = input('Введи какую выручку получила компания \n')
rev_input = int(rev_input)
exp_input = input('Введи сколько компания потратила \n')
exp_input = int(exp_input)
if rev_input > exp_input:
    print('Да ты крут, чувак!')
    profit = rev_input % exp_input
    print('Твоя рентабельность аж: ', profit)
    pers_input = input('А сколько кожаных мешков на тебя работает? \n')
    pers_input = int(pers_input)
    profit_per_person = profit // pers_input
    print('Каждый наш сотрудник принес нам: ', profit_per_person, 'лавэ')
else:
    print('Чувак, мы в жопе!!!')

#Шестое задание
current_distance = input('Введи дисстанцию, которую ты пробежал сегодня \n')
current_distance = int(current_distance)
target_distance = input('Введи свою цель и ты увидишь через сколько дней ты добъешься своей цели при увеличении в 10% каждый день \n')
target_distance = int(target_distance)
day = 1
while current_distance < target_distance:
    current_distance = current_distance * 1.1
    day = day + 1
print('Ну на ', day,'-й день ты достигнешь своего результата, не менее', target_distance, ' км, красавчик!')

#Вот и все