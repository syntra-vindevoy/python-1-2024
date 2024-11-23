import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)
PURPLE = (255, 165, 0)

# Shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
]

# Colors for shapes
SHAPE_COLORS = [CYAN, YELLOW, PURPLE, ORANGE, BLUE, GREEN, RED]

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Clock
clock = pygame.time.Clock()


class Tetris:
    def __init__(self):
        self.board = [
            [0 for _ in range(SCREEN_WIDTH // BLOCK_SIZE)]
            for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)
        ]
        self.current_shape = self.get_new_shape()
        self.next_shape = self.get_new_shape()
        self.shape_color = random.choice(SHAPE_COLORS)
        self.shape_x = SCREEN_WIDTH // BLOCK_SIZE // 2 - len(self.current_shape[0]) // 2
        self.shape_y = 0
        self.game_over = False

    def get_new_shape(self):
        return random.choice(SHAPES)

    def draw_board(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x] != 0:
                    pygame.draw.rect(
                        screen,
                        self.board[y][x],
                        (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
                    )

    def draw_shape(self):
        for y, row in enumerate(self.current_shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        screen,
                        self.shape_color,
                        (
                            (self.shape_x + x) * BLOCK_SIZE,
                            (self.shape_y + y) * BLOCK_SIZE,
                            BLOCK_SIZE,
                            BLOCK_SIZE,
                        ),
                    )

    def move_shape(self, dx, dy):
        self.shape_x += dx
        self.shape_y += dy

    def rotate_shape(self):
        self.current_shape = [list(row) for row in zip(*self.current_shape[::-1])]

    def check_collision(self):
        for y, row in enumerate(self.current_shape):
            for x, cell in enumerate(row):
                if cell:
                    if (
                        self.shape_x + x < 0
                        or self.shape_x + x >= SCREEN_WIDTH // BLOCK_SIZE
                        or self.shape_y + y >= SCREEN_HEIGHT // BLOCK_SIZE
                        or self.board[self.shape_y + y][self.shape_x + x] != 0
                    ):
                        return True
        return False

    def freeze_shape(self):
        for y, row in enumerate(self.current_shape):
            for x, cell in enumerate(row):
                if cell:
                    self.board[self.shape_y + y][self.shape_x + x] = self.shape_color
        self.current_shape = self.next_shape
        self.next_shape = self.get_new_shape()
        self.shape_color = random.choice(SHAPE_COLORS)
        self.shape_x = SCREEN_WIDTH // BLOCK_SIZE // 2 - len(self.current_shape[0]) // 2
        self.shape_y = 0
        if self.check_collision():
            self.game_over = True

    def clear_lines(self):
        new_board = [row for row in self.board if any(cell == 0 for cell in row)]
        lines_cleared = len(self.board) - len(new_board)
        self.board = [
            [0 for _ in range(SCREEN_WIDTH // BLOCK_SIZE)] for _ in range(lines_cleared)
        ] + new_board

    def update(self):
        self.shape_y += 1
        if self.check_collision():
            self.shape_y -= 1
            self.freeze_shape()
            self.clear_lines()

    def draw(self):
        screen.fill(BLACK)
        self.draw_board()
        self.draw_shape()
        pygame.display.flip()


def main():
    game = Tetris()
    while not game.game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move_shape(-1, 0)
                    if game.check_collision():
                        game.move_shape(1, 0)
                elif event.key == pygame.K_RIGHT:
                    game.move_shape(1, 0)
                    if game.check_collision():
                        game.move_shape(-1, 0)
                elif event.key == pygame.K_DOWN:
                    game.move_shape(0, 1)
                    if game.check_collision():
                        game.move_shape(0, -1)
                elif event.key == pygame.K_UP:
                    game.rotate_shape()
                    if game.check_collision():
                        game.rotate_shape()
                        game.rotate_shape()
                        game.rotate_shape()

        game.update()
        game.draw()
        clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    main()
