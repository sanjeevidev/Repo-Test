import chess

board = chess.Board()

for i in board.legal_moves:
    print(i)

board.push_san("e5")
board.push_san("e4")

print(board)
