import pygame
import random
import math

pygame.init()

# frames per second
FPS = 60

# grid display
WIDTH, HEIGHT = 800, 800
ROWS = 4
COLS = 4

#tile height
RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS

OUTLINE_COLOR = (201, 66, 56)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (252, 165, 157)
FONT_COLOR = (119, 110, 101)

FONT = pygame.font.SysFont("comicsans", 60, bold=True)
#speed of tiles
MOVE_VEL = 20

#for menu
MENU_TITLE_COLOR = (92, 20, 14)
MENU_TEXT_COLOR = (119, 110, 101)

TITLE_FONT_SIZE = 80
MENU_FONT_SIZE = 40

