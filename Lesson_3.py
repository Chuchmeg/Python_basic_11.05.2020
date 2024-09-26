#Первое задание

def my_func(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = 0
    return result

print(my_func(int(input("Введи число a: \n")), int(input("Введи число b: \n"))))

#Второе задание

def my_func2(name, lastname, bdyear, city, email, phone):
    print(f"Имя - {name}, Фамилия - {lastname}, Год рождения - {bdyear}, Город проживания - {city}, email - {email}, Телефон - {phone}")

my_func2(name= 'Ренат', lastname='Гарифуллин', bdyear=1989, city='Наб.Челны', email='kukuruza@gmail.com', phone='89274569898')

#Третье задание

def my_func3(x, y, z):
    digits = [x, y, z]
    total = []
    max_1 = max(digits)
    total.append(max_1)
    digits.remove(max_1)
    max_2 = max(digits)
    total.append(max_2)
    print(sum(total))
my_func3(18, 34, 12)

#Четвертое задание

def my_func4(num1, num2):
    return 1 / num1 ** abs(num2)
print(my_func4(2, -1))


def my_func4_1(num3, num4):
    result_num = 1
    for i in range(abs(num4)):
        result_num *= num3
    if num4 >= 0:
        return result_num
    else:
        return 1 / result_num
print(my_func4_1(2, -1))

#Пятое задание

def my_sum ():
    total_result = 0
    exit = False
    while exit == False:
        input_number = input('Введи числа. Для выхода введи Q - ').split()

        current_result = 0
        for el in range(len(input_number)):
            if input_number[el] == 'q' or input_number[el] == 'Q':
                exit = True
                break
            else:
                current_result = current_result + int(input_number[el])
        total_result = total_result + current_result
        print(f'Текущая сумма: {total_result}')
    print(f'Окончательная сумма:  {total_result}')
my_sum()

#Шестое задание

def int_func (*args):
    input_words = input("Введи слово или слова \n")
    print(input_words.title())
    return
int_func()
