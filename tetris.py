import pygame
import sys
from game import Game
from colors import Colors

pygame.init()

# Setting up the presentation of the game itself
title = pygame.font.Font(None, 42)
scores = title.render("Score", True, Colors.white)
nextup = title.render("Next", True, Colors.white)
youdied = title.render("GAME OVER", True, Colors.red)

scoreboard = pygame.Rect(320, 55, 170, 60)
comingsoon = pygame.Rect(320, 220, 170, 180)

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Tetris")

fps = pygame.time.Clock()

game = Game()

gameupdate = pygame.USEREVENT
pygame.time.set_timer(gameupdate, 250)

# Manages all of the possible "events" in the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.gameover == True:
                game.gameover = False
                game.reset()
            if event.key == pygame.K_LEFT and game.gameover == False:
                game.moveleft()
            if event.key == pygame.K_RIGHT and game.gameover == False:
                game.moveright()
            if event.key == pygame.K_DOWN and game.gameover == False:
                game.movedown()
                game.scoring(0, 1)
            if event.key == pygame.K_UP and game.gameover == False:
                game.rotate()
        # This is so the blocks fall down much slower, as opposed to 60 times per second
        if event.type == gameupdate and game.gameover == False:
            game.movedown()

    showscore = title.render(str(game.score), True, Colors.white)
    screen.fill(Colors.bluebg)
    screen.blit(scores, (365, 20, 50, 50))
    screen.blit(nextup, (375, 180, 50, 50))

# Adds a "GAME OVER" if you fail, game resets upon a new input
    if game.gameover == True:
        screen.blit(youdied, (320, 450, 50, 50))
        
    pygame.draw.rect(screen, Colors.gray, scoreboard, 0, 10)
    screen.blit(showscore, showscore.get_rect(centerx = scoreboard.centerx, centery = scoreboard.centery))
    pygame.draw.rect(screen, Colors.gray, comingsoon, 0, 10)

    game.draw(screen)

    pygame.display.update()
    # Setting the ticks (or frames per second) to 60 fps
    fps.tick(60)
