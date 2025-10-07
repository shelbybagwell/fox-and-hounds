import copy
import math

import numpy as np
from gameboard.board import GameBoard


def evaluate_for_hounds(board: GameBoard):
    isTerminal = board.check_win()
    if isTerminal == "HOUNDS":
        return 1e9
    if isTerminal == "FOX":
        return -1e9
    fr, fc = np.argwhere(board.board == 2)[0]
    goalC, goalR = (5, 1)
    dist_goal = max(abs(goalR - fr), abs(goalC - fc))
    fox_moves = len(board.get_available_moves("FOX"))
    hounds_ahead = sum(
        1 for (hr, hc) in np.argwhere(board.board == 1) if hr <= fr
    )
    return 6.0 * dist_goal - 4.0 * fox_moves + 2.0 * hounds_ahead


def _apply_hound_move_clone(board: GameBoard, move):
    new_board = copy.deepcopy(board)
    (fr, fc), (tr, tc) = move
    new_board.board[tr, tc] = 1
    new_board.board[fr, fc] = 0
    new_board.current_player = "FOX"
    return new_board


def _fox_pos(board: GameBoard):
    pos = np.argwhere(board.board == 2)
    return tuple(pos[0]) if len(pos) else None


def _apply_fox_move_clone(board: GameBoard, to_pos):
    nb = copy.deepcopy(board)
    pos = _fox_pos(nb)
    if pos is None:
        print(f"Error, could not apply move")
        return board
    fr, fc = pos
    tr, tc = to_pos
    nb.board[tr, tc] = 2
    nb.board[fr, fc] = 0
    nb.current_player = "HOUNDS"
    return nb


def Hounds_Minimax_AI(board: GameBoard, depth: int = 4):
    def max_value(board: GameBoard, depth, alpha, beta):
        isTerminal = board.check_win()
        if isTerminal is not None or depth == 0:
            return evaluate_for_hounds(board), None

        best_val, best_move = -math.inf, None
        for move in board.get_available_moves("HOUNDS"):
            new_board = _apply_hound_move_clone(board, move)
            val, _ = min_value(new_board, depth - 1, alpha, beta)
            if val > best_val:
                best_val, best_move = val, move
            alpha = max(alpha, best_val)
            if alpha >= beta:
                break
        return best_val, best_move

    def min_value(board: GameBoard, depth, alpha, beta):
        isTerminal = board.check_win()
        if isTerminal is not None or depth == 0:
            return evaluate_for_hounds(board), None

        best_val = math.inf
        for move in board.get_available_moves("FOX"):
            new_board = _apply_fox_move_clone(board, move)
            val, _ = max_value(new_board, depth - 1, alpha, beta)
            if val < best_val:
                best_val = val
            beta = min(beta, best_val)
            if alpha >= beta:
                break
        return best_val, None

    _, move = max_value(board, depth, -math.inf, math.inf)
    return move


def Hounds_Random_AI(board):
    moves = board.legal_hound_moves()
    if not moves:
        return None
    import random

    return random.choice(moves)
