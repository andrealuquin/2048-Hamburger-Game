import pygame

from settings import (
    ROWS,
    COLS,
    WIDTH,
    HEIGHT,
    RECT_WIDTH,
    RECT_HEIGHT,
    OUTLINE_COLOR,
    OUTLINE_THICKNESS,
    BACKGROUND_COLOR,
)

def draw_grid(window):
    for row in range(1, ROWS):
        y = row * RECT_HEIGHT
        pygame.draw.line(window, OUTLINE_COLOR, (0, y), (WIDTH,y), OUTLINE_THICKNESS)
    for col in range(1, COLS):
        x = col * RECT_WIDTH
        pygame.draw.line(window, OUTLINE_COLOR, (x, 0), (x, HEIGHT), OUTLINE_THICKNESS)

    pygame.draw.rect(window, OUTLINE_COLOR, (0, 0, WIDTH, HEIGHT), OUTLINE_THICKNESS)

# draws updated grid display
def draw (window, tiles):
    game_background = pygame.image.load("assets/images/game_background.png")
    game_background = pygame.transform.scale(game_background, (WIDTH, HEIGHT))
    window.blit(game_background, (0, 0))
    window.fill(BACKGROUND_COLOR)

    for tile in tiles.values():
        tile.draw(window)

    draw_grid(window) 

    pygame.display.update()