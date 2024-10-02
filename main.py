from dataclasses import dataclass
from random import randint

import pygame

import config

pygame.init()

screen = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)

width = screen.get_width()
height = screen.get_height()

background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, (width, height))


@dataclass
class Snowflake:
    x: int
    y: float
    size: int
    speed_y: int
    speed_x: int
    color: list[int]


snowflakes = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    if randint(0, 1) == 0:
        size = randint(config.MIN_SIZE, config.MAX_SIZE)
        color = [config.COLOR_SNOWFLAKE() for _ in range(3)]
        speed_y = (size - config.MIN_SIZE) / (config.MAX_SIZE - config.MIN_SIZE) + 1

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
        snowflake.y += snowflake.speed_y + config.WIND_SPEED[0]
        snowflake.x += snowflake.speed_x + config.WIND_SPEED[1]

        if snowflake.y > height:
            del snowflake

    pygame.display.flip()

pygame.quit()
