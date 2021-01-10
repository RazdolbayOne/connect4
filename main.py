import numpy as np  # Helps in using methods for making and adding functionality to a matrix
import pygame
import sys
import math

# TODO NEEED TO REFACTOR ALL!!!!!!!!!!!!!!!!!!!!!!!!!!!
import random
ROW_COUNT = 6  # Global Static Variable
COLUMN_COUNT = 7  # These are the rows and colums specified before the program begins

BLUE_COLOR = (0, 0, 255)  # Its an RGB value (here only blue has some value)
BLACK_COLOR = (0, 0, 0)  # Black value in RGB is (0,0,0)
RED_COLOR = (255, 0, 0)
YELLOW_COLOR = (255, 255, 0)  # YELLOW is a combination of both red and green
SQUARE_SIZE = 100  # The value of each square is in pixels


# def main():
#    pass

def create_board():
    board = np.zeros(
        (ROW_COUNT, COLUMN_COUNT))  # Makes a matrix of 6 x 7 of all zeros (np.zeros(x,y) produces a matrix)
    return board


def drop_piece(board, row, col, chip):
    """places chip on specific row and col pos in board"""
    board[row][col] = chip  # fills the slot with the piece


def is_valid_col(board, col):
    """Checking to make sure that the column has not been filled fully,
     it checks the last row only (it returns a boolean value)"""
    return board[ROW_COUNT - 1][col] == 0


def get_valid_bottom_row_of_col(board, col):
    """return most lower row of specific col"""
    for row in range(ROW_COUNT):
        if board[row][col] == 0:  # returns the slot which empty ,1st case which is empty
            return row


def print_board(board):
    """ To make the board build from the bottom up"""
    # 0 is the axis i.e. flip the board over x axis, right side up (np.flip() is a command in numpy)
    print(np.flip(board, 0))
    print("---------------------------------------")


def is_winning_state(board, piece):
    """Check if after placing chip winning state  appiered
       4 dots are in line(either horizontally,vertically and diagonally)
    """
    # Check horizontal locations for win
    for cols in range(COLUMN_COUNT - 3):  # we're subtracting 3 since the logic is applicable for 4 columns only
        for r in range(ROW_COUNT):
            if (board[r][cols] == piece and board[r][cols + 1] == piece and board[r][cols + 2] == piece and board[r][
                cols + 3] == piece):
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):  # we're subtracting 3 since the logic is applicable for 4 columns only3
            if (board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece):
                return True

    # Check positively sloped diagonals
    for c in range(COLUMN_COUNT - 3):  # we're subtracting 3 so that the logic works for 4 columns
        for r in range(ROW_COUNT - 3):  # we're subtracting 3 since the logic is applicable for 4 columns only
            if (board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece):
                return True

    # Check negatively sloped diagonals
    for c in range(
            COLUMN_COUNT - 3):  # Remember the the index of the matrix starts from the lower side since we have flipped the matrix
        for r in range(3,
                       ROW_COUNT):  # Here the negatively sloped diagonal cannot start any lower than the 3 index(i.e. 0,1,2 indices)
            if (board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece):
                return True


def draw_board(board):
    """ draws in using pygame board"""
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(game_window, BLUE_COLOR, (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE,
                                                       SQUARE_SIZE))  # These are the (screen size,positon on y-axis,width,height)
            pygame.draw.circle(game_window, BLACK_COLOR, (
                int(c * SQUARE_SIZE + SQUARE_SIZE / 2), int(r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)),
                               chip_radius)  # pygame accepts only integers (refer pygame documentation)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(game_window, RED_COLOR, (
                    int(c * SQUARE_SIZE + SQUARE_SIZE / 2), screen_height - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)),
                                   chip_radius)
            elif board[r][c] == 2:
                pygame.draw.circle(game_window, YELLOW_COLOR, (
                    int(c * SQUARE_SIZE + SQUARE_SIZE / 2), screen_height - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)),
                                   chip_radius)

    pygame.display.update()  # so that the screen is updated after each click


board = create_board()
print_board(board)
turn = 0

# every pygame project i.e. it initializes the pygame module
pygame.init()

# Defining the screen size
screen_width = COLUMN_COUNT * SQUARE_SIZE  # Its the number of columns times the square_size
screen_height = (ROW_COUNT + 1) * SQUARE_SIZE  # One additional row for displaying the spot where we are dropping the circle

size = (screen_width, screen_height)  # size is a tuple of width and height

chip_radius = int(SQUARE_SIZE / 2 - 5)  # radius has to be a little smaller than the squaresize

game_window = pygame.display.set_mode(size)  # for pygame to read size  (from documentation)

draw_board(board)

# Whenever we want to update  display
pygame.display.update()

my_font = pygame.font.SysFont("monospace", 75)  # Refer the documentation ()
game_over = False
while not game_over:
    # pygame is an event based library it reads every key or mouse-click pressed as an event
    for event in pygame.event.get():

        pygame.display.update()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(game_window, BLACK_COLOR, (0, 0, screen_width, SQUARE_SIZE))
            mouse_click_pos_x = event.pos[0]  # This provides the position of the cursor
            if turn == 0:
                pygame.draw.circle(game_window, RED_COLOR, (mouse_click_pos_x, int(SQUARE_SIZE / 2)), chip_radius)
            else:
                pass
                # pygame.draw.circle(game_window, YELLOW_COLOR, (mouse_click_pos_x, int(SQUARE_SIZE / 2)), chip_radius)

        if event.type == pygame.QUIT:  # Done in every game, it allows us to properly exit out of any game
            sys.exit()  # system exit (when we click on exit sign it should close)

        # Where click it drops down the piece in that place
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(game_window, BLACK_COLOR, (0, 0, screen_width, SQUARE_SIZE))

            # Ask for Player 1 Input
            if (turn == 0):
                mouse_click_pos_x = event.pos[0]  # the initial position
                col = int(math.floor(mouse_click_pos_x / SQUARE_SIZE))  # The player enters the column no. here
                if is_valid_col(board, col):
                    row = get_valid_bottom_row_of_col(board, col)
                    drop_piece(board, row, col, 1)

                    if is_winning_state(board, 1):
                        label = my_font.render("Player 1 wins!!!", 1, RED_COLOR)  # The font will be printed in "red"
                        game_window.blit(label,
                                         (40, 10))  # It updates text to the specific part(position) of the screen
                        game_over = True  # It ends the game
                print_board(board)
                draw_board(board)  # need re draw_board after every turn

                turn += 1  # increase each term  by one
                turn = turn % 2  # It alternates between player 1 and player 2
                pygame.time.wait(100)


            # Ask for Player 2 Input
            else:
                pass
                #col=random.randint(0, COLUMN_COUNT)
                #row = get_valid_bottom_row_of_col(board, col)
                #drop_piece(board, row, col, 2)
                """
                # the initial position
                mouse_click_pos_x = event.pos[0]
                # calc in which col chip will be placed
                col = int(math.floor(mouse_click_pos_x / SQUARE_SIZE))

                # check if it possible to place in colon the  chip
                if is_valid_col(board, col):
                    # get most_valid_bottom row of colomn
                    row = get_valid_bottom_row_of_col(board, col)
                    #places chip at cpecific coords
                    drop_piece(board, row, col, 2)

                    if is_winning_state(board, 2):
                        label = my_font.render("Player 2 AI wins!!", 1, YELLOW_COLOR)
                        game_window.blit(label, (40, 10))
                        game_over = True  # It ends the game"""


            #print_board(board)
            #draw_board(board)  # need re draw_board after every turn

            #turn += 1  # increase each term  by one
            #turn = turn % 2  # It alternates between player 1 and player 2

        #AI turn
        if turn !=0:
            col = random.randint(0, COLUMN_COUNT - 1)
            row = get_valid_bottom_row_of_col(board, col)
            drop_piece(board, row, col, 2)

            #print_board(board)
            draw_board(board)  # need re draw_board after every turn

            turn += 1  # increase each term  by one
            turn = turn % 2  # It alternates between player 1 and player 2

        if game_over:
            pygame.time.wait(3000)  # The wait value is in millisecond hence here the wait is 3 seconds

# if __name__ == "__main__":
# execute only if run as a script
#    main()
