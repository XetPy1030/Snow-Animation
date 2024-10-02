from random import randint

# Size of the snowflakes
MIN_SIZE = 3
MAX_SIZE = 6

# Color of the snowflakes
COLOR_SNOWFLAKE = lambda: randint(200, 255)

# Speed of the snowflakes
MIN_SPEED = 7
MAX_SPEED = 11

# Wind speed, offset for the snowflakes
OFFSET_X = -300
WIND_SPEED = [1.5, 1]

FPS = 60

# Chance of a new snowflake
CHANCE_NEW_SNOWFLAKE = 50
