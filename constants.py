# Game constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
BOARD_SIZE = 8
SQUARE_SIZE = WINDOW_WIDTH // BOARD_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_SQUARE = (240, 217, 181)  # Light brown
DARK_SQUARE = (181, 136, 99)    # Dark brown
HIGHLIGHT = (247, 247, 105)     # Yellow highlight
MOVE_HINT = (106, 168, 79, 150) # Green transparent for possible moves

# Chess piece values (for AI)
PAWN_VALUE = 10
KNIGHT_VALUE = 30
BISHOP_VALUE = 30
ROOK_VALUE = 50
QUEEN_VALUE = 90
KING_VALUE = 900

# Asset paths
PIECE_IMAGES_PATH = "assets/pieces/"
