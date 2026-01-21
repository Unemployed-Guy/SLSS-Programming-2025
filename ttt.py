# Tic Tac Toe
# Author: Tyson
# January 14 2026

import pygame

pygame.init()

# COLOURS - (R, G, B)
# CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
WHITE = (255, 255, 255)

def game():

    pygame.init()

    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Tic Tac Toe")

    WIDTH = 600
    HEIGHT = 600

    BOARD = pygame.image.load("assets/board.webp")
    X_IMG = pygame.image.load("assets/x.png")
    O_IMG = pygame.image.load("assets/o.png")

    done = False
    player = "X"

    screen.fill(WHITE)
    screen.blit(BOARD, (64, 64))
    CELL_SIZE = (BOARD.get_width() // 3)

    BOARD_X = (screen.get_width() - BOARD.get_width()) // 2
    BOARD_Y = (screen.get_height() - BOARD.get_height()) // 2

    board = [
    ["","",""],
    ["","",""],
    ["","",""]
    ]

    def get_cell_from_mouse(pos):
        x, y = pos

        if x < BOARD_X or y < BOARD_Y: # (AI HELP) Ignores the clicks not on board
                return None

        col = (x - BOARD_X) // CELL_SIZE # (AI HELP) Moves to the position on grid
        row = (y - BOARD_Y) // CELL_SIZE

        if row > 2 or col > 2:
            return None

        return row, col

    # AI was used here, I will explain
    def draw_board():
        # Use both width and height to calculate cell size
        cell_size_w = BOARD.get_width() // 3
        cell_size_h = BOARD.get_height() // 3
        CELL_SIZE = min(cell_size_w, cell_size_h)  # ensures it fits both directions

        # Resize X/O images to fit in the cell (80%)
        target_size = int(CELL_SIZE * 0.8)
        X_resized = pygame.transform.smoothscale(X_IMG, (target_size, target_size))
        O_resized = pygame.transform.smoothscale(O_IMG, (target_size, target_size))

        # Offset to center
        x_offset = (CELL_SIZE - target_size) // 2
        y_offset = (CELL_SIZE - target_size) // 2

        for row in range(3):
            for col in range(3):
                cell_x = BOARD_X + col * CELL_SIZE
                cell_y = BOARD_Y + row * CELL_SIZE

                if board[row][col] == "X":
                    screen.blit(X_resized, (cell_x + x_offset, cell_y + y_offset))
                elif board[row][col] == "O":
                    screen.blit(O_resized, (cell_x + x_offset, cell_y + y_offset))


    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                                cell = get_cell_from_mouse(event.pos)
                                if cell:
                                    row, col = cell
                                    if board[row][col] == "":
                                        board[row][col] = player
                                        player = "O" if player == "X" else "X"

        screen.fill(WHITE)
        screen.blit(BOARD, (BOARD_X, BOARD_Y))
        draw_board()
        pygame.display.flip()

if __name__ == "__main__":
    game()
