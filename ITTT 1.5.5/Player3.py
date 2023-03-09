import pygame
import Field
import Colors

# pygame.init()

# определяем количество игроков и длину ряда
# players_count = int(input('Введите количество игроков'))
players_lst = []


# row_length = int(input('Введите длину ряда, который надо выложить игроку'))


class Player:
    def __init__(self, num):  # num - номер игрока
        self.num = num
        self.color = Colors.colors[self.num - 1]
        # self.wins = wins  кол-во побед
        # self.games = games  кол-во игр
        self.occup_cells = []
        # self.row = 0

    def motion(self):
        x_mouse, y_mouse = pygame.mouse.get_pos()
        x_cell = x_mouse - (x_mouse - 6) % 33
        y_cell = y_mouse - (y_mouse - 6) % 33
        cell_num = ((x_cell - 6) // 33) * 24 + ((y_cell - 6) // 33 + 1)  # вычисляем номер клетки
        if getattr(Field.cells[cell_num - 1], 'occupation') != 0:
            return 1  # again
        else:
            Field.cells[cell_num - 1].cell_occupation(self.num)
            print(cell_num, 'номер клетки')
            self.occup_cells.append(Field.cells[cell_num - 1])
            # condition = self.check(cell_num)
            if self.check(cell_num) == 2:
                return 2
            else:
                return 3

    def check(self, cell_num):
        if self._count_horizontal(cell_num) or self._count_vertical(cell_num) or self._count_left_diagonal(cell_num) or self._count_right_diagonal(cell_num):
            return 2  # finish
        else:
            return 3  # next

    # функции проверки ряда

    def _count_horizontal(self, cell_num):
        count = 1
        last_num = cell_num
        for _ in range(5):
            if self.is_my_right(cell_num):
                count += 1
                cell_num += 24
        for _ in range(5):
            if self.is_my_left(last_num):
                count += 1
                last_num -= 24
        if count >= 5:
            return True
        else:
            return False

    def _count_vertical(self, cell_num):
        count = 1
        last_num = cell_num
        for _ in range(5):
            if self.is_my_up(cell_num):
                count += 1
                cell_num += 1
        for _ in range(5):
            if self.is_my_down(last_num):
                count += 1
                last_num -= 1
        if count >= 5:
            return True
        else:
            return False

    def _count_right_diagonal(self, cell_num):
        count = 1
        last_num = cell_num
        for _ in range(5):
            if self.is_my_right_down(cell_num):
                count += 1
                cell_num += 23
        for _ in range(5):
            if self.is_my_left_up(last_num):
                count += 1
                last_num -= 23
        if count >= 5:
            return True
        else:
            return False

    def _count_left_diagonal(self, cell_num):
        count = 1
        last_num = cell_num
        for _ in range(5):
            if self.is_my_right_up(cell_num):
                count += 1
                cell_num += 25
        for _ in range(5):
            if self.is_my_left_down(last_num):
                count += 1
                last_num -= 25
        if count >= 5:
            return True
        else:
            return False

    # функции проверки клетки

    def is_my_right(self, cell_num):
        if cell_num <= 1081:
            if Field.cells[cell_num + 23] in self.occup_cells:
                return True
            else:
                return False
        else:
            return False

    def is_my_left(self, cell_num):
        if cell_num >= 23:
            if Field.cells[cell_num - 25] in self.occup_cells:
                return True
            else:
                return False
        else:
            return False

    def is_my_up(self, cell_num):
        if cell_num <= 1103:
            if Field.cells[cell_num] in self.occup_cells:
                return True
            else:
                return False
        else:
            return False

    def is_my_down(self, cell_num):
        if cell_num >= 1:
            if Field.cells[cell_num - 2] in self.occup_cells:
                return True
            else:
                return False
        else:
            return False

    def is_my_left_up(self, cell_num):
        if cell_num >= 24:
            if Field.cells[cell_num - 24] in self.occup_cells:
                return True
            else:
                return False
        else:
            return False

    def is_my_right_down(self, cell_num):
        if cell_num <= 1082:
            if Field.cells[cell_num + 22] in self.occup_cells:
                return True
            else:
                return False
        else:
            return False

    def is_my_right_up(self, cell_num):
        if cell_num <= 1080:
            if Field.cells[cell_num + 24] in self.occup_cells:
                return True
            else:
                return False
        else:
            return False

    def is_my_left_down(self, cell_num):
        if cell_num >= 26:
            if Field.cells[cell_num - 26] in self.occup_cells:
                return True
            else:
                return False
        else:
            return False


for i in range(3):
    players_lst.append(Player(i + 1))
