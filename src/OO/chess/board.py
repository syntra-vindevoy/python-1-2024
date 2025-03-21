class Piece:
    def __init__(self, color):
        """
        Base class for chess pieces.
        :param color: 'white' or 'black'
        """
        self.color = color

    def is_valid_move(self, start, end, board):
        """
        Abstract method to check if a move is valid.
        Should be overridden by each specific piece type.
        :param start: The starting position (row, col).
        :param end: The ending position (row, col).
        :param board: Reference to the board for validation.
        """
        raise NotImplementedError("This method should be overridden in derived classes.")

    def __str__(self):
        """
        String representation of the piece.
        """
        return f"{self.color} {self.__class__.__name__}"


class Pawn(Piece):

    def is_valid_move(self, start, end, board):
        """
        Validates pawn movement.
        Pawns move forward one square, or two on their first move.
        Can only capture diagonally.
        """
        start_row, start_col = start
        end_row, end_col = end
        direction = 1 if self.color == 'white' else -1  # White moves up, black moves down

        # Normal move
        if start_col == end_col and end_row == start_row + direction:
            return board.grid[end_row][end_col] is None  # Must be an empty square

        # Double move on first turn
        if start_col == end_col and start_row == (6 if self.color == 'white' else 1):
            if end_row == start_row + (2 * direction) and board.grid[end_row][end_col] is None:
                return True

        # Capturing diagonally
        if abs(start_col - end_col) == 1 and end_row == start_row + direction:
            return isinstance(board.grid[end_row][end_col], Piece) and board.grid[end_row][
                end_col].color != self.color  # Must capture an opponent's piece

        return False


class Rook(Piece):

    def is_valid_move(self, start, end, board):
        """
        Validates rook movement (straight lines: horizontal or vertical).
        """
        start_row, start_col = start
        end_row, end_col = end

        # Either the row or the column must remain the same
        if start_row != end_row and start_col != end_col:
            return False

        # Check if the path between start and end is clear
        if start_row == end_row:  # Horizontal move
            # Check all columns between start and end
            step = 1 if start_col < end_col else -1
            for col in range(start_col + step, end_col, step):
                if board.grid[start_row][col] is not None:
                    return False
        else:  # Vertical move
            # Check all rows between start and end
            step = 1 if start_row < end_row else -1
            for row in range(start_row + step, end_row, step):
                if board.grid[row][start_col] is not None:
                    return False

        # The destination must either be empty or occupied by an opponent's piece
        destination = board.grid[end_row][end_col]
        return destination is None or destination.color != self.color


class Board:
    def __init__(self):
        """
        Initialize the chessboard as an 8x8 grid with None (empty squares).
        """
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()

    def setup_board(self):
        """
        Place all pieces in their starting positions.
        """
        # Place pawns
        for col in range(8):
            self.grid[1][col] = Pawn('black')  # Black pawns
            self.grid[6][col] = Pawn('white')  # White pawns

        # Place rooks
        self.grid[0][0] = self.grid[0][7] = Rook('black')
        self.grid[7][0] = self.grid[7][7] = Rook('white')

        # Other pieces can be added here (knights, bishops, etc.)

    def move_piece(self, start, end):
        """
        Move a piece from start to end position if the move is valid.
        :param start: (row, col) of the piece to move.
        :param end: (row, col) of the destination.
        """
        piece = self.grid[start[0]][start[1]]
        if piece is None:
            raise ValueError("No piece at the start position.")

        if not piece.is_valid_move(start, end, self):
            raise ValueError("Invalid move for this piece.")

        # Execute the move
        self.grid[end[0]][end[1]] = piece
        self.grid[start[0]][start[1]] = None


# Initialize board
board = Board()

# Print initial board setup
for row in board.grid:
    print([str(piece) if piece else '.' for piece in row])

# Move a pawn
board.move_piece((6, 0), (4, 0))  # Valid move: white pawn moves forward two squares
for row in board.grid:
    print([str(piece) if piece else '.' for piece in row])
