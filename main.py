import pygame
import math
import random

pygame.init()

WIN = pygame.display.set_mode((600, 400))
CLOCK = pygame.time.Clock()
SQUARE_SIZE = 75
SPEED = 0.5
COLOR_LIST = ['red', 'blue', 'purple', 'black', 'white', 'green']

def color_swap(color):
    background.blit(scrolling_surface(SQUARE_SIZE, SQUARE_SIZE))
    color_filter.fill(color)
    background.blit(color_filter)

def create_color_filter(surface, opacity):
    color_filter_surface = pygame.Surface((surface.width, surface.height))
    color_filter_surface.set_alpha(opacity)
    return color_filter_surface

def scrolling_surface(square_width, square_height):
    column_amount = math.ceil(WIN.width / square_width) + 2
    row_amount = math.ceil(WIN.height / square_height) + 2
    full_surface = pygame.Surface((column_amount * square_width, row_amount * square_height))
    last_coords = [0, 0]
    color_switcher = True

    for row in range(1, row_amount):
        last_coords[0] = 0
        if row % 2 == 0:
            color_switcher = False
        else:
            color_switcher = True

        for column in range(1, column_amount):
            square = pygame.Surface((square_width, square_height))
            if color_switcher:
                square.fill("#808080")
            else:
                square.fill("#c0c0c0")

            full_surface.blit(square, last_coords)
            last_coords[0] += square_width
            color_switcher = not color_switcher
            
        last_coords[1] += square_height

    return full_surface

def scrolling_animation(speed, square_size):
    background_coords[1] -= speed
    background_coords[0] -= speed

    if background_coords[0] == -square_size:
        background_coords[0] = 0
    if background_coords[1] == -square_size:
        background_coords[1] = 0
    
background = scrolling_surface(SQUARE_SIZE, SQUARE_SIZE)
color_filter = create_color_filter(background, 100)
background_coords = [0, 0]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            color_swap(random.choice(COLOR_LIST))
    
    scrolling_animation(SPEED, SQUARE_SIZE)
    WIN.blit(background, background_coords)

    pygame.display.update()
    CLOCK.tick(60)
