import pygame
import math

from settings import RECT_WIDTH, RECT_HEIGHT, FONT, FONT_COLOR


def load_tile_images():

    image_paths = {
        2: "assets/images/plate.png",
        4: "assets/images/bottom_bun.png",
        8: "assets/images/meat.png",
        16: "assets/images/cheese.png",
        32: "assets/images/lettuce.png",
        64: "assets/images/tomatos.png",
        128: "assets/images/onions.png",
        256: "assets/images/ketchup.png",
        512: "assets/images/mustard.png",
        1024: "assets/images/meat2.png",
        2048: "assets/images/top_bun.png",
    }

    tile_images = {}

    for value, path in image_paths.items():
        image = pygame.image.load(path).convert_alpha()
        image = pygame.transform.scale(image, (RECT_WIDTH, RECT_HEIGHT))
        tile_images[value] = image

    return tile_images


TILE_IMAGES = {}