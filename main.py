import pygame
from visualizer.constants import SIZE, SQUARE_SIZE, GAP
from visualizer.board import Board

window = pygame.display.set_mode((SIZE, SIZE))
FPS = 60
pygame.display.set_caption("idk")


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // (SQUARE_SIZE + GAP)
    col = x // (SQUARE_SIZE + GAP)
    return row, col


def main():
    play = True
    clock = pygame.time.Clock()
    board = Board()

    # main loop
    while play:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                # print(row, col)
                board.add_comp(col, row)

            # redraw function
            board.draw_grid(window)
            pygame.display.update()

    pygame.quit()


main()
