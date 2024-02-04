import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
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
                # Если клетка выбрана, то она закрашивается полностью
                color = 'white'
                if self.board[j][i] == 1:
                    color = 'blue'
                pygame.draw.rect(screen, color, (
                    (self.left + self.cell_size * i,
                     self.top + self.cell_size * j),
                    (self.cell_size,
                     self.cell_size)), width=1)

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

    def on_click(self, cell_coords):
        i, j = cell_coords
        if self.board[i][j] == 0:
            self.board[i][j] = 1
        else:
            self.board[i][j] = 0

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)



pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)

pygame.display.set_caption('Игрулька')
# CОздаём игровое поле
board = Board(5, 7)
board.set_view(100, 100, 50)

# Запускаем игровой цикл
running = True
while running:
    #  Обработка входящих событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # board.get_click(event.pos)
            active_cell = board.get_cell(event.pos)
            print(active_cell)

    # Отрисовка
    # Очищаем экран
    screen.fill('black')
    # Отрисовываем поле
    board.render(screen)
    # Обновлям экран
    pygame.display.flip()
