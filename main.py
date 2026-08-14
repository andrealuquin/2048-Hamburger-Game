import pygame
from settings import WIDTH, HEIGHT, FPS
from drawing import draw
from movement import generate_tiles, move_tiles
from menu import draw_menu


#For loading music 
def load_music():
    try:
        pygame.mixer.music.load("assets/music/theme.mp3")
        pygame.mixer.music.set_volume(0.4)
    except pygame.error:
        print("Could not load music file.")


def main():
    pygame.init()
    pygame.mixer.init()
    
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("2048 Hamburger Game")

    load_music()

    clock = pygame.time.Clock()
    run = True

    #game starts on menu screen
    game_state = "menu"

    
    music_on = False

    #tiles are generated but board resets when player starts
    tiles = generate_tiles()

    while run:
        clock.tick(FPS)

        # Drawing section
        if game_state == "menu":
            draw_menu(window, music_on)
        elif game_state == "playing":
            draw(window, tiles)

        # Event handling section
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                # Menu controls
                if game_state == "menu":

                    # enter starts a new game
                    if event.key == pygame.K_RETURN:
                        game_state = "playing"
                        tiles = generate_tiles()
                    # m turn the music on or off
                    elif event.key == pygame.K_m:
                        music_on = not music_on
                        if music_on:
                            pygame.mixer.music.play(-1)
                        else:
                            pygame.music.stop()
                #game controls
                if event.key == pygame.K_LEFT:
                    move_tiles(window, tiles, clock, "left")

                elif event.key == pygame.K_RIGHT:
                    move_tiles(window, tiles, clock, "right")

                elif event.key == pygame.K_UP:
                    move_tiles(window, tiles, clock, "up")

                elif event.key == pygame.K_DOWN:
                    move_tiles(window, tiles, clock, "down")

    pygame.quit()


if __name__ == "__main__":
    main()