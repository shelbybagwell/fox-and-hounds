from gameboard.board import GameBoard
import random   # for random move selection
import numpy as np

my_board = GameBoard()


# # lets just get the fox to have a single random move.
# available_moves = my_board.get_available_moves("FOX") 
# print("Available moves for FOX:")
# print(available_moves)        
# # move the fox with the first option
# move = available_moves[0]
# print(f"Making move {move}")
# my_board.move_piece(move[0], move[1])
# print(my_board.board)

# my_board.render_board()


def Fox_Random_AI(board):
    available_moves = board.get_available_moves("FOX")
    move = random.choice(available_moves)
    return move

def dijkstra(board):
    fox_pos = np.argwhere(board == 2)
    fox_r, fox_c = fox_pos[0]
    # target is bottom right
    target = (5, 5)
    # create set of unvisited nodes
    unvisited = set()
    for r in range(6):
        for c in range(6):
            if board[r, c] == 0:  # only consider dark squares
                unvisited.add((r, c))
    unvisited.add((fox_r, fox_c)) # add fox position to unvisited
    # ensure that the target is in unvisited
    if target not in unvisited:
        print("Target position is not reachable.")
        return []
    # initialize distances
    distances = {pos: float('inf') for pos in unvisited}
    distances[(fox_r, fox_c)] = 0
    previous_nodes = {pos: None for pos in unvisited}
    while unvisited:
        current = min(unvisited, key=lambda pos: distances[pos])
        if current == target or distances[current] == float('inf'):
            break
        unvisited.remove(current)
        r, c = current
        neighbors = [(r + dr, c + dc) for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]]
        for nr, nc in neighbors:
            if (nr, nc) in unvisited:
                alt = distances[current] + 1
                if alt < distances[(nr, nc)]:
                    distances[(nr, nc)] = alt
                    previous_nodes[(nr, nc)] = current
    path = []
    current = target
    while current and current in previous_nodes:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()
    return path


# because the hounds cannot move yet, we will just move the fox around
# for ten moves.
# for i in range(10):
#     fox_random_move = Fox_Random_AI(my_board)
#     my_board.move_piece(fox_random_move[0], fox_random_move[1])
#     print(my_board.board)
#     my_board.render_board()
#     print(available_moves)


# one single move with dijkstra
# path = dijkstra(my_board.board)
# print("Dijkstra path for fox to (5,5):")
# print(path)
# if len(path) > 1:
#     next_move = path[1]  # the first element is the current position
#     fox_pos = np.argwhere(my_board.board == 2)
#     fox_r, fox_c = fox_pos[0]
#     my_board.move_piece((fox_r, fox_c), next_move)
#     print("Board after Dijkstra move:")
#     print(my_board.board)
#     my_board.render_board()
# else:
#     print("No path found for fox to reach target.")
#     next_move = Fox_Random_AI(my_board)
#     my_board.move_piece(next_move[0], next_move[1])
#     print("Board after random move:")
#     print(my_board.board)
#     my_board.render_board()

def Fox_Short_Path_AI(board):
    path = dijkstra(board.board)
    if len(path) > 1:
        next_move = path[1]  # the first element is the current position
        fox_pos = np.argwhere(board.board == 2)
        fox_r, fox_c = fox_pos[0]
        return ( (fox_r, fox_c), next_move )
    else:
        return Fox_Random_AI(board)


# because the hounds cannot move yet, we will just move the fox around
# for ten moves.
for i in range(10):
    fox_ssp_move = Fox_Short_Path_AI(my_board)
    print(f"fox pos: {fox_ssp_move[0]}, next move: {fox_ssp_move[1]}")
    print(my_board.check_win())
    if my_board.check_win() in ["FOX", "HOUNDS"]:
        print("Game Over!")
        break
    my_board.move_piece(fox_ssp_move[0], fox_ssp_move[1])
    print(my_board.board)
    my_board.render_board()