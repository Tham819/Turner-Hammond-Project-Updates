import pygame
from colors import Colors
from position import Position

class Tetromino:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cellsize = 30
        self.rowoffset = 0
        self.coloffset = 0
        self.rotatestage = 0
        self.colors = Colors.get_colors()

    def move(self, rows, columns):
        self.rowoffset += rows
        self.coloffset += columns

    def get_positions(self):
        tiles = self.cells[self.rotatestage]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.rowoffset, position.col + self.coloffset)
            moved_tiles.append(position)
        return moved_tiles
    
    def rotate(self):
        self.rotatestage += 1
        if self.rotatestage == len(self.cells):
            self.rotatestage = 0

    def unrotate(self):
        self.rotatestage -= 1
        if self.rotatestage == -1:
            self.rotatestage = len(self.cells) -1

    def draw(self, screen, xoffset, yoffset):
        tiles = self.get_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(xoffset + tile.col * self.cellsize, yoffset + tile.row * self.cellsize, self.cellsize -1, self.cellsize -1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
