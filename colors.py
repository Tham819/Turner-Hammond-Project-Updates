import pygame

class Colors:
    gray = pygame.Color('gray15')
    cyan = pygame.Color('aqua')
    yellow = pygame.Color('yellow1')
    purple = pygame.Color('purple')
    green = pygame.Color('lime')
    blue = pygame.Color('blue1')
    red = pygame.Color('red1')
    orange = pygame.Color('orange')
    white = pygame.Color('white')
    bluebg = pygame.Color('royalblue4')

    @classmethod
    def get_colors(cls):
        return [cls.gray, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]
