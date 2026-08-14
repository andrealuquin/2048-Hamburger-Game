import pygame
from settings import (
    WIDTH,
    BACKGROUND_COLOR,
    MENU_TITLE_COLOR,
)


def draw_centered_text(window, text, font, color, y):
    rendered_text = font.render(text, True, color)
    x = WIDTH / 2 - rendered_text.get_width() / 2
    window.blit(rendered_text, (x, y))


def draw_button(window, rect, text, font, mouse_pos):
    if rect.collidepoint(mouse_pos):
        button_color = (255, 220, 130)
    else:
        button_color = (242, 175, 90)

    outline_color = (92, 20, 14)
    text_color = (92, 20, 14)

    pygame.draw.rect(window, button_color, rect, border_radius=20)
    pygame.draw.rect(window, outline_color, rect, width=5, border_radius=20)

    rendered_text = font.render(text, True, text_color)

    text_x = rect.x + (rect.width - rendered_text.get_width()) / 2
    text_y = rect.y + (rect.height - rendered_text.get_height()) / 2

    window.blit(rendered_text, (text_x, text_y))


def draw_menu(window):
    window.fill(BACKGROUND_COLOR)

    title_font = pygame.font.SysFont("comicsans", 80, bold=True)
    button_font = pygame.font.SysFont("comicsans", 45, bold=True)

    mouse_pos = pygame.mouse.get_pos()

    draw_centered_text(
        window,
        "2048 Burger",
        title_font,
        MENU_TITLE_COLOR,
        180,
    )

    play_button = pygame.Rect(250, 360, 300, 90)

    draw_button(
        window,
        play_button,
        "PLAY",
        button_font,
        mouse_pos,
    )

    pygame.display.update()

    return play_button