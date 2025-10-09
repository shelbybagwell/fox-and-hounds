import math

def evaluate_for_hounds(board) -> float:
    """Heuristic score (higher = better for Hounds)."""
    term = board.is_terminal()
    if term == 'HOUNDS': return 1e9
    if term == 'FOX':    return -1e9

    fr, fc = board.fox
    gr, gc = (5, 5)  # FOX_GOAL on a 6x6
    dist_goal = max(abs(gr - fr), abs(gc - fc))      # farther fox is from goal, the better
    fox_moves = len(board.legal_fox_moves())         # fewer fox moves, the better
    hounds_ahead = sum(1 for (hr, hc) in board.hounds if hr <= fr)  # more ranks ahead, the better
    return 6.0*dist_goal - 4.0*fox_moves + 2.0*hounds_ahead

def _apply_move_clone(board, move, player: str):
    """Lightweight clone+apply to avoid mutating original during search."""
    nb = board.clone()
    if player == 'HOUNDS':
        nb.apply_hound_move(move)
    else:
        nb.apply_fox_move(move)
    return nb

def Hounds_Minimax_AI(board, depth: int = 4):
    """Stronger Hounds AI using minimax with alpha–beta pruning (depth-configurable)."""
    assert board.turn == 'HOUNDS'

    def max_value(b, d, alpha, beta):
        term = b.is_terminal()
        if term is not None or d == 0:
            return evaluate_for_hounds(b), None

        best_val, best_mv = -math.inf, None
        for mv in b.legal_hound_moves():
            nb = _apply_move_clone(b, mv, 'HOUNDS')
            val, _ = min_value(nb, d-1, alpha, beta)
            if val > best_val:
                best_val, best_mv = val, mv
            alpha = max(alpha, best_val)
            if alpha >= beta:  # prune
                break
        return best_val, best_mv

    def min_value(b, d, alpha, beta):
        term = b.is_terminal()
        if term is not None or d == 0:
            return evaluate_for_hounds(b), None

        best_val = math.inf
        for mv in b.legal_fox_moves():
            nb = _apply_move_clone(b, mv, 'FOX')
            val, _ = max_value(nb, d-1, alpha, beta)
            if val < best_val:
                best_val = val
            beta = min(beta, best_val)
            if alpha >= beta:  # prune
                break
        return best_val, None

    _, move = max_value(board, depth, -math.inf, math.inf)
    return move

def Hounds_Minimax_AI_d4(board):
    """Named callable wrapper for depth=4."""
    return Hounds_Minimax_AI(board, depth=4)
