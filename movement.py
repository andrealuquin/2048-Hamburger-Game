# movement.py

import random
from settings import ROWS, COLS, RECT_WIDTH, RECT_HEIGHT, MOVE_VEL, FPS
from tile import Tile
from drawing import draw


def get_tile_key(row, col):
    return f"{row}{col}"


def get_random_pos(tiles):
    while True:
        row = random.randrange(0, ROWS)
        col = random.randrange(0, COLS)

        if get_tile_key(row, col) not in tiles:
            break

    return row, col


def move_tiles(window, tiles, clock, direction):
    updated = True
    blocks = set()

    if direction == "left":
        sort_func = lambda tile: tile.col
        reverse = False
        delta = (-MOVE_VEL, 0)
        boundary_check = lambda tile: tile.col == 0
        get_next_tile = lambda tile: tiles.get(get_tile_key(tile.row, tile.col - 1))
        merge_check = lambda tile, next_tile: tile.x > next_tile.x + MOVE_VEL
        move_check = lambda tile, next_tile: tile.x > next_tile.x + RECT_WIDTH + MOVE_VEL
        ceil = True

    elif direction == "right":
        sort_func = lambda tile: tile.col
        reverse = True
        delta = (MOVE_VEL, 0)
        boundary_check = lambda tile: tile.col == COLS - 1
        get_next_tile = lambda tile: tiles.get(get_tile_key(tile.row, tile.col + 1))
        merge_check = lambda tile, next_tile: tile.x < next_tile.x - MOVE_VEL
        move_check = lambda tile, next_tile: tile.x + RECT_WIDTH + MOVE_VEL < next_tile.x
        ceil = False

    elif direction == "up":
        sort_func = lambda tile: tile.row
        reverse = False
        delta = (0, -MOVE_VEL)
        boundary_check = lambda tile: tile.row == 0
        get_next_tile = lambda tile: tiles.get(get_tile_key(tile.row - 1, tile.col))
        merge_check = lambda tile, next_tile: tile.y > next_tile.y + MOVE_VEL
        move_check = lambda tile, next_tile: tile.y > next_tile.y + RECT_HEIGHT + MOVE_VEL
        ceil = True

    elif direction == "down":
        sort_func = lambda tile: tile.row
        reverse = True
        delta = (0, MOVE_VEL)
        boundary_check = lambda tile: tile.row == ROWS - 1
        get_next_tile = lambda tile: tiles.get(get_tile_key(tile.row + 1, tile.col))
        merge_check = lambda tile, next_tile: tile.y < next_tile.y - MOVE_VEL
        move_check = lambda tile, next_tile: tile.y + RECT_HEIGHT + MOVE_VEL < next_tile.y
        ceil = False

    else:
        return "continue"

    moved = False

    while updated:
        clock.tick(FPS)
        updated = False
        sorted_tiles = sorted(tiles.values(), key=sort_func, reverse=reverse)

        for i, tile in enumerate(sorted_tiles):
            if boundary_check(tile):
                continue

            next_tile = get_next_tile(tile)

            if not next_tile:
                tile.move(delta)

            elif (
                tile.value == next_tile.value
                and tile not in blocks
                and next_tile not in blocks
            ):
                if merge_check(tile, next_tile):
                    tile.move(delta)
                else:
                    next_tile.value *= 2
                    sorted_tiles.pop(i)
                    blocks.add(next_tile)

            elif move_check(tile, next_tile):
                tile.move(delta)

            else:
                continue

            tile.set_pos(ceil)
            updated = True
            moved = True

        update_tiles(window, tiles, sorted_tiles)

    if moved:
        return end_move(tiles)

    return "continue"


def end_move(tiles):
    if len(tiles) == ROWS * COLS:
        return "lost"

    row, col = get_random_pos(tiles)
    tiles[get_tile_key(row, col)] = Tile(random.choice([2, 4]), row, col)

    return "continue"


def update_tiles(window, tiles, sorted_tiles):
    tiles.clear()

    for tile in sorted_tiles:
        tiles[get_tile_key(tile.row, tile.col)] = tile

    draw(window, tiles)


def generate_tiles():
    tiles = {}

    for _ in range(2):
        row, col = get_random_pos(tiles)
        tiles[get_tile_key(row, col)] = Tile(2, row, col)

    return tiles