import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


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
        board[5, 3] = 1
        board[4, 4] = 1
        board[5, 5] = 1
        board[3, 5] = 1

        # Set up initial fox
        board[0, 0] = 2  # top left corner

        return board

    def move_piece(self, start_pos, end_pos):
        # check if move is valid
        avail_moves = self.get_available_moves(self.current_player)
        if (start_pos, end_pos) not in avail_moves:
            print(
                f"ERROR: Player {self.current_player} - Invalid move: {start_pos} to {end_pos}"
            )
            return False

        # update board state
        piece = self.board[start_pos]
        self.board[end_pos] = piece
        self.board[start_pos] = 0  # spot is now empty

        # switch player turn
        winner = self.check_win()
        if winner:
            # do something
            pass
        # commenting this out for now, I want to
        # just move the fox around
        # if self.current_player == "FOX":
        #     self.current_player = "HOUNDS"
        # else:
        #     self.current_player = "FOX"

        return True

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
                and (self.board[nr, nc] == 0  # space is unoccupied 
                     or self.board[nr, nc] == -1)  # light square
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
        fox_pos = np.argwhere(self.board == 2)
        fox_r, fox_c = fox_pos[0]

        # is fox at the end?
        if fox_r == 5:
            self.game_over = True
            winner = "FOX"
            return winner

        # can fox not move anymore?
        if self.current_player == "FOX":
            fox_moves = self.get_available_moves("FOX")
            if not fox_moves:
                self.game_over = True
                winner = "HOUNDS"

        # nobody wins yet
        return None

    def render_board(self):
        fig, ax = plt.subplots(figsize=(6, 6))

        cmap = ListedColormap(["black", "white"])
        board_display = np.zeros((self.board_size, self.board_size))
        for r in range(self.board_size):
            for c in range(self.board_size):
                board_display[r, c] = (r + c) % 2

        ax.imshow(board_display, cmap=cmap, interpolation="nearest")

        for r in range(self.board_size):
            for c in range(self.board_size):
                if self.board[r, c] == 1:
                    ax.scatter(
                        c,
                        r,
                        color="blue",
                        s=500,
                        edgecolors="black",
                        linewidth=2,
                    )
                elif self.board[r, c] == 2:
                    ax.scatter(
                        c,
                        r,
                        color="red",
                        s=500,
                        edgecolors="black",
                        linewidth=2,
                    )

        ax.set_xticks(np.arange(self.board_size))
        ax.set_yticks(np.arange(self.board_size))
        ax.set_title(f"Turn: {self.current_player}")
        plt.show()
