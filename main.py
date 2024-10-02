import random

import pygame

import config


class Snowflake(pygame.sprite.Sprite):
    """
    This class represents the snowflake.

    It derives from the "Sprite" class in Pygame.
    """

    containers = None

    def __init__(self, x, y, size, color, height):
        super().__init__(self.containers)

        # Create the snowflake
        self.image = pygame.Surface([size * 2, size * 2])
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.image, color, (size, size), size)

        # Set the position of the snowflake
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Set the speed of the snowflake based on its size
        self.speed_y = (size - config.MIN_SIZE) / (config.MAX_SIZE - config.MIN_SIZE) + 1
        # Set the height of the screen for the snowflake to disappear
        self.height = height

    def update(self):
        self.rect.y += self.speed_y + config.WIND_SPEED[0]
        self.rect.x += config.WIND_SPEED[1]
        if self.rect.y > self.height:
            self.kill()


def main():
    # Initialize Pygame
    pygame.init()

    # Set up the screen
    screen = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)

    # Get screen dimensions
    width = screen.get_width()
    height = screen.get_height()

    # Set up the background
    background = pygame.image.load('background.jpg')
    background = pygame.transform.scale(background, (width, height))

    # Initialize Groups
    snowflakes = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    # Add the sprite to the groups
    Snowflake.containers = snowflakes, all_sprites

    # Create clock
    clock = pygame.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background, (0, 0))

        all_sprites.update()

        # Generate new snowflakes
        if random.randint(0, 100) < config.CHANCE_NEW_SNOWFLAKE:
            size = random.randint(config.MIN_SIZE, config.MAX_SIZE)
            color = [config.COLOR_SNOWFLAKE() for _ in range(3)]
            x = random.randint(config.OFFSET_X, width)
            Snowflake(x, -30, size, color, height)

        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(config.FPS)


if __name__ == '__main__':
    main()
    pygame.quit()
