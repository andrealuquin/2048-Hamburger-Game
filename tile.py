import pygame
import random
import os
import math

TILE_IMAGES = {
    2: pygame.image.load("assets/images/plate.png"),
    4: pygame.image.load("assets/images/bottom_bun.png"),
    8: pygame.image.load("assets/images/meat.png"),
    16: pygame.image.load("assets/images/cheese.png"),
    32: pygame.image.load("assets/images/lettuce.png"),
    64: pygame.image.load("assets/images/tomatos.png"),
    128: pygame.image.load("assets/images/onions.png"),
    256: pygame.image.load("assets/images/ketchup.png"),
    512: pygame.image.load("assets/images/mustard.png"),
    1024: pygame.image.load("assets/images/meat2.png"),
    2048: pygame.image.load("assets/images/top_bun.png"),
}
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
              # if this tile value has an image, draw the image on top.
        if self.value in TILE_IMAGES:
            image = TILE_IMAGES[self.value]
            image = pygame.transform.scale(image, (RECT_WIDTH, RECT_HEIGHT))
            window.blit(image, (self.x, self.y))

        # if there is no image yet, draw the number.
        else:
            text = FONT.render(str(self.value), 1, FONT_COLOR)
            window.blit(
                text,
                (
                    self.x + (RECT_WIDTH / 2 - text.get_width() / 2),
                    self.y + (RECT_HEIGHT / 2 - text.get_height() / 2),
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