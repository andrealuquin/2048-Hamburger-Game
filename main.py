import pygame
from settings import WIDTH, HEIGHT, FPS
from drawing import draw, load_drawing_assets
from movement import generate_tiles, move_tiles
from menu import draw_menu


def main():
    pygame.init()

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("2048 Hamburger Game")

    load_drawing_assets()

    clock = pygame.time.Clock()
    run = True

    game_state = "menu"

    # create the starting tiles.
    # this will be reset again when the player clicks Play
    tiles = generate_tiles()

    #this will store the clickable Play button rectangle
    play_button = None

    while run:
        clock.tick(FPS)

        #draw the correct screen depending on the current game state
        if game_state == "menu":
            play_button = draw_menu(window)

        elif game_state == "playing":
            draw(window, tiles)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            #check mouse clicks.
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left click

                    # if we are on the menu and the player clicks Play,
                    # switch to the game screen.
                    if game_state == "menu":
                        if play_button and play_button.collidepoint(event.pos):
                            game_state = "playing"
                            tiles = generate_tiles()

            #check keyboard input
            if event.type == pygame.KEYDOWN:

                #arrow keys should only move tiles during gameplay
                if game_state == "playing":

                    if event.key == pygame.K_LEFT:
                        move_tiles(window, tiles, clock, "left")

                    elif event.key == pygame.K_RIGHT:
                        move_tiles(window, tiles, clock, "right")

                    elif event.key == pygame.K_UP:
                        move_tiles(window, tiles, clock, "up")

                    elif event.key == pygame.K_DOWN:
                        move_tiles(window, tiles, clock, "down")

                    # ESC returns to the menu.
                    elif event.key == pygame.K_ESCAPE:
                        game_state = "menu"

    pygame.quit()


if __name__ == "__main__":
    main()