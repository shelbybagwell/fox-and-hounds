def Hounds_Random_AI(board):
    """Uniformly choose one legal hound move at random."""
    moves = board.legal_hound_moves()
    if not moves:
        return None
    import random
    return random.choice(moves)
