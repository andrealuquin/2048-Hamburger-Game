import pygame
import random
import math

# for each tile: value, row and column position on board
# and pixel position for dreawing 
from settings import RECT_WIDTH, RECT_HEIGHT, FONT, FONT_COLOR
class Tile:
    COLORS = [
        (242, 175, 170),
        (242, 139, 131),
        (237, 92, 81),
        (237, 54, 40),
        (235, 36, 21),
        (143, 14, 4),
        (107, 10, 2),
        (92, 20, 14),
        (94, 32, 26),
    ]
        
    def __init__ (self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.x = col * RECT_WIDTH
        self.y = row * RECT_HEIGHT


    #title value decide which color to use
    def get_color(self):
        color_index = int(math.log2(self.value)) - 1
        color = self.COLORS[color_index]
        return color

    def draw(self, window):
        color = self.get_color()
        pygame.draw.rect(window,color, (self.x, self.y, RECT_WIDTH, RECT_HEIGHT))

        text = FONT.render(str(self.value), 1, FONT_COLOR)

        window.blit(
            text,
            (
            (self.x + (RECT_WIDTH / 2 - text.get_width() / 2)),
            (self.y + (RECT_HEIGHT / 2 - text.get_height() / 2)),
            ),  
        )
 
    def set_pos(self, ceil= False):
        if ceil:
            self.row = math.ceil(self.y / RECT_HEIGHT )
            self.col = math.ceil(self.x / RECT_WIDTH )
        else:
             self.row = math.floor(self.y / RECT_HEIGHT)
             self.col = math.floor(self.x / RECT_WIDTH)

    def move(self, delta):
        self.x += delta[0]
        self.y += delta[1]