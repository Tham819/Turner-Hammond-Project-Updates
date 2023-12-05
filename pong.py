import pygame
import sys
import random

def ball_moving():
    global hor_speed, ver_speed, player_score, opponent_score

    ball.x += hor_speed
    ball.y += ver_speed

    if ball.top <= 0 or ball.bottom >= screen_height:
        ver_speed *= -1

    # For if the Player scores
    if ball.left <= 0:
        ball_start()
        player_score += 1

    # For if the Opponent scores
    if ball.right >= screen_width:
        ball_start()
        opponent_score += 1

    if ball.colliderect(player) or ball.colliderect(opponent):
        hor_speed *= -1

def player_move():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_move():
    if opponent.top < ball.y:
        opponent.y += opponent_speed
    if opponent.bottom > ball.y:
        opponent.y -= opponent_speed
    
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_start():
    global hor_speed, ver_speed
    ball.center = (screen_width/2, screen_height/2)
    ver_speed *= random.choice((1,-1))
    hor_speed += random.choice((1,-1))

pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

bgcolor = pygame.Color('grey12')
itemcolor = pygame.Color('grey68')

ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10,140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10,140)

hor_speed = 5 * random.choice((1,-1))
ver_speed = 5 * random.choice((1,-1))
player_speed = 0
opponent_speed = 5

player_score = 0
opponent_score = 0
basic_font = pygame.font.Font('freesansbold.ttf', 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= 6
            if event.key == pygame.K_DOWN:
                player_speed += 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 6
            if event.key == pygame.K_DOWN:
                player_speed -= 6

    ball_moving()
    player_move()
    opponent_move()

    screen.fill(bgcolor)
    pygame.draw.rect(screen, itemcolor, player)
    pygame.draw.rect(screen, itemcolor, opponent)
    pygame.draw.rect(screen, itemcolor, ball)
    pygame.draw.aaline(screen, itemcolor, (screen_width / 2, 0), (screen_width / 2, screen_height))

    player_text = basic_font.render(f'{player_score}',False,itemcolor)
    screen.blit(player_text,(660,470))

    opponent_text = basic_font.render(f'{opponent_score}',False,itemcolor)
    screen.blit(opponent_text,(600,470))

    pygame.display.flip()
    clock.tick(60)
