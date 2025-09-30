import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm


class GameBoard:
    def __init__(self):
        # create 6x6 board
        # place fox and 4 hounds in starting positions
        # set first turn to fox
        self.board_size = 6
        self.board = self._make_board()

    def _make_board(self):
        # 6x6 board
        board = np.zeros((self.board_size, self.board_size))
        for r in range(self.board_size):
            for c in range(self.board_size):
                if (r + c) % 2 == 1:
                    board[r, c] = -1  # light square, all 0s are dark

        # Set up Initial Hounds
        board[5, 0] = 1
        board[5, 2] = 1
        board[5, 4] = 1
        board[4, 1] = 1

        # Set up initial fox
        board[0, 5] = 2  # top corner

        return board

    def move_piece(self, start_pos, end_pos):
        # check if move is valid
        # update board state
        # switch player turn
        return

    def get_available_moves(self, player):
        # get all valid moves on board for specified player
        # may not need if AIs handle this logic
        return

    def check_win(self):
        # to be run after each move
        # FOX wins if road is pos-5
        # HOUNDS win if no available moves
        # return None if no winner yet
        return

    def render_board(self):
        # plot board and display
        return
