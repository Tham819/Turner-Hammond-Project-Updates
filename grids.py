import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.rows = 20
        self.cols = 10
        self.cellsize = 30
        self.grid = [[0 for j in range(self.cols)] for i in range(self.rows)]
        self.colors = Colors.get_colors()
                     
    def print_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.grid[row][col], end = " ")
            print()

    def inside(self, row, column):
        if row >= 0 and row < self.rows and column >= 0 and column < self.cols:
            return True
        return False
    
    def empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False
    
    def full(self, row):
        for column in range(self.cols):
            if self.grid[row][column] == 0:
                return False
        return True
    
    def clear(self, row):
        for column in range(self.cols):
            self.grid[row][column] = 0

    def gravityrow(self, row, rows):
        for column in range(self.cols):
            self.grid[row+rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def clearfull(self):
        completed = 0
        for row in range(self.rows-1, 0, -1):
            if self.full(row):
                self.clear(row)
                completed += 1
            elif completed > 0:
                self.gravityrow(row, completed)
        return completed
    
    def reset(self):
        for row in range(self.rows):
            for column in range(self.cols):
                self.grid[row][column] = 0
    
    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(col*self.cellsize +11, row*self.cellsize +11, self.cellsize -1, self.cellsize -1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
