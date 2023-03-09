import pygame
import Colors

# pygame.init()

size = (1527, 801)
cell_size, wall_size = 30, 3
cells = []
x, y = 6, 6

# создаем экран
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Ultimate Tic Tac Toe')
screen.fill(Colors.field_col)


class Field:
    def __init__(self, x, y):
        self.occupation = 0
        self.x = x
        self.y = y

    def drawing_cell(self):
        pygame.draw.rect(screen, Colors.cell_col, (self.x, self.y, cell_size, cell_size))

    def cell_occupation(self, num):  # добавить параметр номер игрока
        # if self.occupation == 0:
        pygame.draw.rect(screen, Colors.colors[num - 1], (self.x, self.y, cell_size, cell_size))  # red изменить на coln
        self.occupation = num
        # Player.players_lst[num - 1].occup_cells.append((self.x, self.y))
        # else:
        # вызов главной функции снова


def game_finish():
    screen.fill(Colors.field_col)
    # cells.clear()


def drawing_field():
    ind = 0
    global x
    global y
    for i in range(46):
        for j in range(24):
            cells.append(Field(x, y))
            cells[ind].drawing_cell()
            ind += 1
            y += cell_size + wall_size
        x += cell_size + wall_size
        y = 6
    # print(ind)


# play = True
# while play:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             play = False
#
#     drawing_field()
#     pygame.display.update()
