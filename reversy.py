import pygame
from random import randint

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[randint(0, 1) for _ in range(self.width)] for _ in range(self.height)]
        # Знчения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # Настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, 'white', (
                    (self.left + self.cell_size * i,
                     self.top + self.cell_size * j),
                    (self.cell_size,
                     self.cell_size)), width=1)
                # Если клетка выбрана, то она закрашивается полностью
                color = 'blue'
                if self.board[j][i] == 1:
                    color = 'red'
                pygame.draw.circle(screen, color,
                                   (self.left + self.cell_size * i + self.cell_size // 2,
                                    self.top + self.cell_size * j + self.cell_size // 2),
                                   self.cell_size // 2 - 4, width=0)

    def get_cell(self, mouse_pos):
        # Проверка наличия мыши в пределах поля
        if (mouse_pos[0] < self.left or mouse_pos[0] > (self.left + self.width * self.cell_size) or
                mouse_pos[1] < self.top or mouse_pos[1] > (self.top + self.height * self.cell_size)):
            return None

        # Находим столбец
        cell = [0, 0]
        for i in range(self.width):
            if mouse_pos[0] < self.left + self.cell_size * (i + 1):
                cell[1] = i
                break

        # Находим строку
        for i in range(self.height):
            if mouse_pos[1] < self.top + self.cell_size * (i + 1):
                cell[0] = i
                break

        return tuple(cell)

    def on_click(self, cell_cords, color):
        i, j = cell_cords
        for i in range(self.height):
            self.board[i][j] = color

        i, j = cell_cords
        for j in range(self.width):
            self.board[i][j] = color

    def get_click(self, mouse_pos):
        global color
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell, color)
            color = (color + 1) % 2


pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)

pygame.display.set_caption('Игрулька')
# Coздаём игровое поле
n = int(input())
board = Board(n, n)
board.set_view(100, 100, 50)

# Запускаем игровой цикл
running = True
color = 0
while running:
    #  Обработка входящих событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            board.get_click(event.pos)

    # Отрисовка
    # Очищаем экран
    screen.fill('black')
    # Отрисовываем поле
    board.render(screen)
    # Обновлям экран
    pygame.display.flip()
