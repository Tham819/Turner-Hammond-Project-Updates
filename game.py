from grids import Grid
from blocks import *
import random
import pygame

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [Hero(), BlueRicky(), OrangeRicky(), Smashboy(), RhodeIslandZ(), Teewee(), ClevelandZ()]
        self.currentblock = self.getrandomblock()
        self.nextblock = self.getrandomblock()
        self.gameover = False
        self.score = 0

    def scoring(self, cleared, truckin):
        if cleared == 1:
            self.score += 100
        elif cleared == 2:
            self.score += 300
        elif cleared == 3:
            self.score += 500
        self.score += truckin
    
    def getrandomblock(self):
        if len(self.blocks) == 0:
            self.blocks = [Hero(), BlueRicky(), OrangeRicky(), Smashboy(), RhodeIslandZ(), Teewee(), ClevelandZ()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def moveleft(self):
        self.currentblock.move(0, -1)
        if self.stayinside() == False or self.fits() == False:
            self.currentblock.move(0,1)

    def moveright(self):
        self.currentblock.move(0, 1)
        if self.stayinside() == False or self.fits() == False:
            self.currentblock.move(0,-1)

    def movedown(self):
        self.currentblock.move(1, 0)
        if self.stayinside() == False or self.fits() == False:
            self.currentblock.move(-1, 0)
            self.blocklock()

    def blocklock(self):
        tiles = self.currentblock.get_positions()
        for position in tiles:
            self.grid.grid[position.row][position.col] = self.currentblock.id
        self.currentblock = self.nextblock
        self.nextblock = self.getrandomblock()
        rowscleared = self.grid.clearfull()
        if rowscleared > 0:
            self.scoring(rowscleared, 0)
        if self.fits() == False:
            self.gameover = True

    def reset(self):
        self.grid.reset()
        self.blocks = [Hero(), BlueRicky(), OrangeRicky(), Smashboy(), RhodeIslandZ(), Teewee(), ClevelandZ()]
        self.currentblock = self.getrandomblock()
        self.nextblock = self.getrandomblock()
        self.score = 0

    def fits(self):
        tiles = self.currentblock.get_positions()
        for tile in tiles:
            if self.grid.empty(tile.row, tile.col) == False:
                return False
        return True

    def rotate(self):
        self.currentblock.rotate()
        if self.stayinside() == False or self.fits() == False:
            self.currentblock.unrotate()

    def stayinside(self):
        tiles = self.currentblock.get_positions()
        for tile in tiles:
            if self.grid.inside(tile.row, tile.col) == False:
                return False
        return True
    
    def draw(self, screen):
        self.grid.draw(screen)
        self.currentblock.draw(screen, 11, 11)
        self.nextblock.draw(screen, 270, 270)
