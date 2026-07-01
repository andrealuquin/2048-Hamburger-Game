# menu.py

import pygame
from settings import WIDTH, HEIGHT, BACKGROUND_COLOR, MENU_TITLE_COLOR, MENU_TEXT_COLOR


def draw_centered_text(window, text, font, color, y):
    rendered_text = font.render(text, True, color)

    x = WIDTH / 2 - rendered_text.get_width() / 2

    window.blit(rendered_text, (x, y))


def draw_menu(window, music_on):
    window.fill(BACKGROUND_COLOR)

    title_font = pygame.font.SysFont("comicsans", 80, bold=True)
    menu_font = pygame.font.SysFont("comicsans", 40, bold=True)

    draw_centered_text(
        window,
        "2048 "
         "Hamburger",
        title_font,
        MENU_TITLE_COLOR,
        180,
    )

    draw_centered_text(
        window,
        "Press ENTER to Start",
        menu_font,
        MENU_TEXT_COLOR,
        350,
    )

    draw_centered_text(
        window,
        "Press M to Toggle Music",
        menu_font,
        MENU_TEXT_COLOR,
        420,
    )

    music_text = "Music: ON" if music_on else "Music: OFF"

    draw_centered_text(
        window,
        music_text,
        menu_font,
        MENU_TEXT_COLOR,
        490,
    )

    pygame.display.update()