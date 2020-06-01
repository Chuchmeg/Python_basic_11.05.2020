#Первое задание

from time import sleep
class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'Переключение на \n '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(8)
            i += 1
TrafficLight = TrafficLight()
TrafficLight.running()

#Второе задание

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
    def mass(self):
        return self._length * self._width

class MassCount(Road):
    def __init__(self, _length, _width, thickness):
        super().__init__(_length, _width)
        self.thickness = thickness


result = MassCount(5000, 20, 5)
print(result.mass())

#Третье задание

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
    def get_full_name(self):
        return self.name + ' ' + self.surname
    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

a = Position('Вася', 'Пупкин', 'Крысолов', 100000, 20000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())

#Четвертое задание

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f'{self.name} поехала'
    def stop(self):
        return f'{self.name} остановилась'
    def turn_right(self):
        return f'{self.name} поворачивает направо'
    def turn_left(self):
        return f'{self.name} поворачивает налево'
    def show_speed(self):
        return f'Скорость {self.name} сейчас {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f'Скорость Town Car машины {self.name} сейчас {self.speed}')
        if self.speed > 40:
            return f'Превышение скорости у Town Car {self.name} '
        else:
            return f'Скорость норм у {self.name}'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f'Скорость Worker Car машины {self.name} сейчас {self.speed}')
        if self.speed > 60:
            return f'Превышение скорости у Worker Car {self.name}. Тебя лешили премии, опять!!!'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def police(self):
        if self.is_police:
            return f'{self.name} ментовская тачка'
        else:
            return f'{self.name} не ментовская тачка'

QuattroPorte = SportCar(210, 'Gray', 'QuattroPorte', False)
Vesta = TownCar(60, 'White', 'Vesta', False)
Caddy = WorkCar(70, 'Brown', 'Caddy', True)
Explorer = PoliceCar(110, 'Black',  'Explorer', True)
print(Caddy.turn_left())
print(f'Когда {Vesta.turn_right()}, тогда {QuattroPorte.stop()}')
print(f'{Caddy.go()}. {Caddy.show_speed()}')
print(f'{Caddy.name} is {Caddy.color}')
print(f'{QuattroPorte.name} ментовская тачка? {QuattroPorte.is_police}')
print(f'{Caddy.name}  ментовская тачка? {Caddy.is_police}')
print(QuattroPorte.show_speed())
print(Vesta.show_speed())
print(Explorer.police())
print(Explorer.show_speed())

#Пятое задание

class Stationary:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f'Запуск отрисовки {self.title}'

class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'У вас в руках {self.title}.'

class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'У вас в руках {self.title}.'

class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'У вас в руках {self.title}.'

pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())