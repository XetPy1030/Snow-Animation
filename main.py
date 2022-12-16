import pygame
from dataclasses import dataclass
from random import randint
import config

pygame.init()

screen = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)

background = pygame.image.load('./back.jpg')

width = screen.get_width()
height = screen.get_height()

wind = [1.5, 1]

@dataclass
class Snowflake:
    x: int
    y: float
    size: int
    speed_y: int
    speed_x: int
    color: tuple

snowflakes = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen.fill(config.BACKGROUND)
    screen.blit(background, (0, 0))
    
    if randint(0, 1) == 0:
        size = randint(config.MIN_SIZE, config.MAX_SIZE)
        color = [config.COLOR_SNOWFLAKE() for _ in range(3)]
        # speed = randint(config.MIN_SPEED, config.MAX_SPEED)/10
        speed_y = (size-config.MIN_SIZE)/(config.MAX_SIZE-config.MIN_SIZE) + 1

        snowflakes.append(
            Snowflake(
                randint(-300, width),
                -30,
                size,
                speed_y,
                0,
                color
            )
        )
    for snowflake in snowflakes:
        pygame.draw.circle(
            screen,
            snowflake.color,
            (snowflake.x, int(snowflake.y)),
            snowflake.size
        )
        snowflake.y += snowflake.speed_y+wind[0]
        snowflake.x += snowflake.speed_x+wind[1]
        
        # wind[0] = wind[0] - 0.00001 if wind[0] > 0 else wind[0]
        # wind[1] = wind[1] - 0.00001 if wind[1] > 0 else wind[1]
        
        # if randint(0, 200000) == 0:
        #     wind[1] += randint(0, 15)/10
        
        if snowflake.y > height:
            del snowflake

    pygame.display.flip()

pygame.quit()