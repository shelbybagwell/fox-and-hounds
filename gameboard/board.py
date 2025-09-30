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
        self.current_player = "FOX"
        self.game_over = False

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

    def get_piece_moves(self, r, c):
        moves = []
        piece = self.board[r, c]

        # Fox logic
        if piece == 2:
            dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        # Hound logic
        elif piece == 1:
            dirs = [(-1, 1), (-1, 1)]
        else:
            # something went wrong??
            print("ERROR: invalid piece type")
            return []

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < self.board_size  # valid row
                and 0 <= nc < self.board_size  # valid column
                and self.board[nr, nc] == 0  # space is unoccupied
            ):
                moves.append((nr, nc))

        return moves

    def get_available_moves(self, player):
        # get all valid moves on board for specified player
        all_moves = []

        if self.current_player == "FOX":
            piece_val = 2
        else:
            piece_val = 1

        cur_coords = np.argwhere(self.board == piece_val)

        for r, c in cur_coords:
            piece_moves = self.get_piece_moves(r, c)
            for end_pos in piece_moves:
                all_moves.append(((r, c), end_pos))

        return all_moves

    def check_win(self):
        # to be run after each move
        # FOX wins if road is pos-5
        # HOUNDS win if no available moves
        # return None if no winner yet
        return

    def render_board(self):
        # plot board and display
        return
