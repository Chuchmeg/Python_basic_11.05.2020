#Первое задание

class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        one_matrix = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                one_matrix[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in one_matrix]))


    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in one_matrix]))



done_matrix = Matrix([[11, 22, 33],
                    [44, 55, 66],
                    [77, 88, 99]],
                   [[11, 22, 33],
                    [44, 55, 66],
                    [77, 88, 99]])

print(done_matrix.__add__())

#Второе задание

class Textile:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def square_coat(self):
        return self.size / 6.5 + 0.5

    def square_jacket(self):
        return self.height * 2 + 0.3

    @property
    def square_full(self):
        return str(f'Общая площать ткани: \n'
                   f' {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}')

class Coat(Textile):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_c = float(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'На пальто: {self.square_c}'


class Jacket(Textile):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_j = float(self.height * 2 + 0.3)

    def __str__(self):
        return f'На костюм: {self.square_j}'

coat = Coat(52, 33)
jacket = Jacket(52, 33)
print(coat)
print(jacket)
print(coat.square_full)

#Третье задание

class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Отрицательно!')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))


    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row

cells1 = Cell(20)
cells2 = Cell(14)
print(cells1)
print(cells1 + cells2)
print(cells1 - cells2)
print(cells2.make_order(7))
print(cells1.make_order(13))
print(cells1 / cells2)