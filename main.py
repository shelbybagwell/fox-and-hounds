from gameboard.board import GameBoard
import random   # for random move selection

my_board = GameBoard()


# lets just get the fox to have a single random move.
available_moves = my_board.get_available_moves("FOX") 
print("Available moves for FOX:")
print(available_moves)        
# move the fox with the first option
move = available_moves[0]
print(f"Making move {move}")
my_board.move_piece(move[0], move[1])
print(my_board.board)

my_board.render_board()


def Fox_Random_AI(board):
    available_moves = board.get_available_moves("FOX")
    move = random.choice(available_moves)
    return move

# because the hounds cannot move yet, we will just move the fox around
# for ten moves.
for i in range(10):
    fox_random_move = Fox_Random_AI(my_board)
    my_board.move_piece(fox_random_move[0], fox_random_move[1])
    print(my_board.board)
    my_board.render_board()
    print(available_moves)


