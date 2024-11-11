#Tetris - text base code

import random
import os
import time

# Screen size and block shapes
GRID_WIDTH, GRID_HEIGHT = 10, 20
SHAPES = [
    [[1, 1, 1, 1]],  # Line
    [[1, 1], [1, 1]],  # Square
    [[0, 1, 1], [1, 1, 0]],  # S shape
    [[1, 1, 0], [0, 1, 1]],  # Z shape
    [[1, 1, 1], [0, 1, 0]],  # T shape
    [[1, 1, 1], [1, 0, 0]],  # L shape
    [[1, 1, 1], [0, 0, 1]],  # Reverse L shape
]

class Tetris:
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = self.new_piece()
        self.next_piece = self.new_piece()
        self.score = 0
        self.game_over = False

    def new_piece(self):
        shape = random.choice(SHAPES)
        return {'shape': shape, 'x': GRID_WIDTH // 2 - len(shape[0]) // 2, 'y': 0}

    def rotate_piece(self, piece):
        return [list(row)[::-1] for row in zip(*piece['shape'])]

    def can_move(self, dx, dy, piece=None):
        piece = piece or self.current_piece
        for y, row in enumerate(piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    new_x = piece['x'] + x + dx
                    new_y = piece['y'] + y + dy
                    if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT or (new_y >= 0 and self.grid[new_y][new_x]):
                        return False
        return True

    def merge_piece(self):
        for y, row in enumerate(self.current_piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.current_piece['y'] + y][self.current_piece['x'] + x] = 1
        self.clear_rows()
        self.current_piece = self.next_piece
        self.next_piece = self.new_piece()
        if not self.can_move(0, 0):
            self.game_over = True

    def clear_rows(self):
        new_grid = [row for row in self.grid if any(cell == 0 for cell in row)]
        rows_cleared = GRID_HEIGHT - len(new_grid)
        self.score += rows_cleared ** 2
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(rows_cleared)] + new_grid

    def print_grid(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Score: {self.score}")
        for y in range(GRID_HEIGHT):
            line = '|'
            for x in range(GRID_WIDTH):
                if any(
                    0 <= self.current_piece['y'] + py < GRID_HEIGHT and
                    0 <= self.current_piece['x'] + px < GRID_WIDTH and
                    self.current_piece['shape'][py][px]
                    for py, row in enumerate(self.current_piece['shape'])
                    for px, cell in enumerate(row)
                    if cell and self.current_piece['y'] + py == y and self.current_piece['x'] + px == x
                ):
                    line += "X"
                else:
                    line += " " if self.grid[y][x] == 0 else "O"
            line += '|'
            print(line)
        print('-' * (GRID_WIDTH + 2))

    def run(self):
        while not self.game_over:
            self.print_grid()
            time.sleep(0.5)

            # Move down automatically
            if self.can_move(0, 1):
                self.current_piece['y'] += 1
            else:
                self.merge_piece()

            # User input
            move = input("Move (a:left, d:right, s:down, w:rotate): ").lower()
            if move == 'a' and self.can_move(-1, 0):
                self.current_piece['x'] -= 1
            elif move == 'd' and self.can_move(1, 0):
                self.current_piece['x'] += 1
            elif move == 's' and self.can_move(0, 1):
                self.current_piece['y'] += 1
            elif move == 'w':
                rotated_shape = self.rotate_piece(self.current_piece)
                if self.can_move(0, 0, {'shape': rotated_shape, 'x': self.current_piece['x'], 'y': self.current_piece['y']}):
                    self.current_piece['shape'] = rotated_shape

        print("Game Over! Final Score:", self.score)

# Start the game
if __name__ == "__main__":
    game = Tetris()
    game.run()
