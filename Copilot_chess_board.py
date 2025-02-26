class ChessBoard:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        # Create an 8x8 board initialized with empty spaces
        board = [[' ' for _ in range(8)] for _ in range(8)]
        return board

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

# Create a chessboard instance and print it
chess_board = ChessBoard()
chess_board.print_board()
