import pygame
from visualizer.bfs import BFS
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
    drag = -1

    # main loop
    while play:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                drag = event.button
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                if event.button == 1:
                    board.add_remove_comp(col, row)
                elif event.button == 3:
                    board.add_remove_block(col, row)

            if event.type == pygame.MOUSEBUTTONUP:
                drag = -1

            if event.type == pygame.MOUSEMOTION:
                mouse_y, mouse_x = get_row_col_from_mouse(event.pos)
                # print(mouse_x, mouse_y)
                if drag == 1:
                    board.add_remove_comp(mouse_x, mouse_y)
                elif drag == 3:
                    board.add_remove_block(mouse_x, mouse_y)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    bfs = BFS(board)
                    bfs.run()

            # redraw function
            board.draw_grid(window)
            pygame.display.update()

    pygame.quit()


main()
