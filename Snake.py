import pygame
import time
import random
 
snake_speed = 15
 
# Window size
window_x = 720
window_y = 480
 
# Defining the few colors we'll use, using pygame's built-in color library
black = pygame.Color('black')
white = pygame.Color('white')
red = pygame.Color('red2')
green = pygame.Color('green3')
 
# Initializing pygame
pygame.init()
 
# Initializing the game window
pygame.display.set_caption('Snake Pygame')
game_window = pygame.display.set_mode((window_x, window_y))
 
# FPS (frames per second) controller
fps = pygame.time.Clock()
 
# Sets the Snake's default position
snake_position = [100, 50]
 
# Defines the first 4 blocks of the Snake's body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

# Randomizes the food position
food_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
 
food_spawn = True
 
# Sets the Snake's default direction towards the right
direction = 'RIGHT'
change_to = direction
 
# Initial score of 0
score = 0
 
# Function to display the score
def show_score(choice, color, font, size):
   
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)
 
# Game over function
def game_over():

    my_font = pygame.font.SysFont('times new roman', 50)
     

    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
     
    game_over_rect = game_over_surface.get_rect()
     
    game_over_rect.midtop = (window_x/2, window_y/4)
     
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
     
    time.sleep(2)
     
    pygame.quit()

    quit()
 
 
# Main Function
while True:
     
    # Handling the inputs
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
 
    # Just in case two keys are pressed simultaneously
    # The snake moving two directions at once could be a bit troublesome
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    # Controlling the Snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
 
    # Function for scoring & growing
    # If the Snake & food collides, your score will be incremented by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 10
        food_spawn = False
    else:
        snake_body.pop()
         
    if not food_spawn:
        food_position = [random.randrange(1, (window_x//10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10]
         
    food_spawn = True
    game_window.fill(black)
     
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
        
    pygame.draw.rect(game_window, white, pygame.Rect(
        food_position[0], food_position[1], 10, 10))
 
    # Calls it a game over if the Snake goes off-screen
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
 
    # Calls it a game over if the Snake touches itself
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
 
    # Simple program to display your current score
    show_score(1, white, 'times new roman', 20)
 
    # Refreshes the game screen
    pygame.display.update()
 
    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)
