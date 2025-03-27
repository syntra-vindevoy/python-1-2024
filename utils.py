import os
import pygame
from constants import PIECE_IMAGES_PATH, SQUARE_SIZE

# Dictionary to store loaded images
piece_images = {}

def load_piece_images():
    """Load all chess piece images into memory"""
    # Create default piece images (don't try to load from disk)
    create_default_piece_images()

def create_placeholder_image(color, piece):
    """Create a basic placeholder image for pieces"""
    surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
    
    bg_color = (200, 200, 200) if color == 'white' else (50, 50, 50)
    text_color = (50, 50, 50) if color == 'white' else (200, 200, 200)
    
    pygame.draw.rect(surface, bg_color, (0, 0, SQUARE_SIZE, SQUARE_SIZE))
    
    # Add text for piece type
    font = pygame.font.SysFont('Arial', SQUARE_SIZE // 2)
    
    # Use first letter of piece name
    piece_symbol = piece[0].upper()
    if piece == 'knight':  # Use 'N' for knight
        piece_symbol = 'N'
        
    text = font.render(piece_symbol, True, text_color)
    text_rect = text.get_rect(center=(SQUARE_SIZE//2, SQUARE_SIZE//2))
    surface.blit(text, text_rect)
    
    piece_images[f"{color}_{piece}"] = surface

def create_default_piece_images():
    """Create all default piece images"""
    colors = ['white', 'black']
    pieces = ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']
    
    for color in colors:
        for piece in pieces:
            create_placeholder_image(color, piece)

def get_piece_image(color, piece_type):
    """Get the image for a specific piece"""
    key = f"{color.name.lower()}_{piece_type.lower()}"
    return piece_images.get(key)

def position_to_pixels(position):
    """Convert chess position to pixel coordinates"""
    # Note: in our Position class, horizontal is stored as 1-8 (instead of A-H)
    # and vertical is 1-8 where 1 is at the bottom
    
    # Translate to 0-based coordinates with 0,0 at top left
    x = (position.horizontal - 1) * SQUARE_SIZE
    y = (8 - position.vertical) * SQUARE_SIZE
    
    return (x, y)

def pixels_to_position(x, y):
    """Convert pixel coordinates to chess position"""
    from position import Position
    
    # Convert to 0-based coordinates
    col = x // SQUARE_SIZE
    row = y // SQUARE_SIZE
    
    # Convert to Position format
    horizontal = chr(col + 65)  # A-H (65 is ASCII for 'A')
    vertical = 8 - row  # 1-8
    
    return Position(horizontal=horizontal, vertical=vertical)
