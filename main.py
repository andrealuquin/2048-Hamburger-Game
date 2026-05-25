import pygame
from settings import WIDTH, HEIGHT, FPS
from drawing import draw
from movement import generate_tiles, move_tiles


def main():
    pygame.init()

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("2048 Hamburger Game")

    clock = pygame.time.Clock()
    run = True

    tiles = generate_tiles()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_tiles(window, tiles, clock, "left")

                elif event.key == pygame.K_RIGHT:
                    move_tiles(window, tiles, clock, "right")

                elif event.key == pygame.K_UP:
                    move_tiles(window, tiles, clock, "up")

                elif event.key == pygame.K_DOWN:
                    move_tiles(window, tiles, clock, "down")

        draw(window, tiles)

    pygame.quit()


if __name__ == "__main__":
    main()