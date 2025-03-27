from __future__ import annotations
from typing import TYPE_CHECKING, List, Optional
import pygame

from color import Color
from position import Position
from utils import get_piece_image, position_to_pixels

if TYPE_CHECKING:
    from board import Board


class Piece:
    """Base class for all chess pieces"""
    
    def __init__(self, *, color: Color, position: Position):
        self.color = color
        self.position = position
        self.has_moved = False
        self.captured = False
        self.symbol = ""  # Symbol for console representation
        
    def draw(self, surface: pygame.Surface):
        """Draw the piece on the given surface"""
        if self.captured:
            return
            
        img = get_piece_image(self.color, self.__class__.__name__.lower())
        if img:
            x, y = position_to_pixels(self.position)
            surface.blit(img, (x, y))
            
    def valid_move(self, from_pos: Position, to_pos: Position, board: Board) -> bool:
        """Check if the move from from_pos to to_pos is valid"""
        # Base validation for all pieces
        
        # Can't move to the same position
        if from_pos == to_pos:
            return False
            
        # Can't capture own piece
        target_piece = board.get_piece(position=to_pos)
        if target_piece and target_piece.color == self.color:
            return False
            
        return self._is_valid_piece_move(from_pos, to_pos, board)
    
    def _is_valid_piece_move(self, from_pos: Position, to_pos: Position, board: Board) -> bool:
        """Piece-specific movement validation"""
        raise NotImplementedError("_is_valid_piece_move not implemented")
        
    def get_possible_moves(self, board: Board) -> List[Position]:
        """Get all possible moves for this piece on the current board"""
        possible_moves = []
        
        # Check all board positions
        for h in range(1, 9):
            for v in range(1, 9):
                to_pos = Position(horizontal=chr(h + 64), vertical=v)
                if self.valid_move(self.position, to_pos, board):
                    possible_moves.append(to_pos)
                    
        return possible_moves
    
    def move_to(self, to_pos: Position):
        """Move the piece to the new position"""
        self.has_moved = True
        self.position = to_pos


class Pawn(Piece):
    def __init__(self, *, color: Color, position: Position):
        super().__init__(color=color, position=position)
        self.symbol = 'P'
        self.en_passant_vulnerable = False
        
    def _is_valid_piece_move(self, from_pos: Position, to_pos: Position, board: Board) -> bool:
        # Direction of movement (up for white, down for black)
        direction = 1 if self.color.name == "WHITE" else -1
        
        # Calculate position differences
        dx = to_pos.horizontal - from_pos.horizontal
        dy = to_pos.vertical - from_pos.vertical
        
        # Regular move (forward 1 square)
        if dx == 0 and dy == direction and board.get_piece(position=to_pos) is None:
            return True
            
        # Initial double move
        if (dx == 0 and 
            ((self.color.name == "WHITE" and from_pos.vertical == 2 and to_pos.vertical == 4) or
             (self.color.name == "BLACK" and from_pos.vertical == 7 and to_pos.vertical == 5)) and
            not self.has_moved and
            board.get_piece(position=to_pos) is None and
            board.get_piece(position=Position(horizontal=chr(from_pos.horizontal + 64), 
                                             vertical=from_pos.vertical + direction)) is None):
            return True
            
        # Capturing diagonally
        if abs(dx) == 1 and dy == direction:
            target_piece = board.get_piece(position=to_pos)
            
            # Regular capture
            if target_piece and target_piece.color != self.color:
                return True
                
            # En passant capture
            en_passant_pos = Position(horizontal=chr(to_pos.horizontal + 64), vertical=from_pos.vertical)
            en_passant_piece = board.get_piece(position=en_passant_pos)
            
            if (en_passant_piece and 
                isinstance(en_passant_piece, Pawn) and 
                en_passant_piece.color != self.color and
                en_passant_piece.en_passant_vulnerable):
                return True
                
        return False
        
    def move_to(self, to_pos: Position):
        # Check for en passant vulnerability (double move)
        self.en_passant_vulnerable = not self.has_moved and abs(to_pos.vertical - self.position.vertical) == 2
        super().move_to(to_pos)


class Rook(Piece):
    def __init__(self, *, color: Color, position: Position):
        super().__init__(color=color, position=position)
        self.symbol = 'R'
        
    def _is_valid_piece_move(self, from_pos: Position, to_pos: Position, board: Board) -> bool:
        # Rook moves in straight lines (horizontal or vertical)
        if from_pos.horizontal != to_pos.horizontal and from_pos.vertical != to_pos.vertical:
            return False
            
        # Check for pieces in between
        dx = 0 if from_pos.horizontal == to_pos.horizontal else (1 if from_pos.horizontal < to_pos.horizontal else -1)
        dy = 0 if from_pos.vertical == to_pos.vertical else (1 if from_pos.vertical < to_pos.vertical else -1)
        
        current_pos = from_pos
        while True:
            current_pos = Position(
                horizontal=chr(current_pos.horizontal + dx + 64),
                vertical=current_pos.vertical + dy
            )
            
            if current_pos == to_pos:
                break
                
            if board.get_piece(position=current_pos) is not None:
                return False
                
        return True


class Knight(Piece):
    def __init__(self, *, color: Color, position: Position):
        super().__init__(color=color, position=position)
        self.symbol = 'N'  # N for Knight (K is for King)
        
    def _is_valid_piece_move(self, from_pos: Position, to_pos: Position, board: Board) -> bool:
        # Knight moves in L-shape: 2 squares in one direction, then 1 square perpendicular
        dx = abs(to_pos.horizontal - from_pos.horizontal)
        dy = abs(to_pos.vertical - from_pos.vertical)
        
        return (dx == 1 and dy == 2) or (dx == 2 and dy == 1)


class Bishop(Piece):
    def __init__(self, *, color: Color, position: Position):
        super().__init__(color=color, position=position)
        self.symbol = 'B'
        
    def _is_valid_piece_move(self, from_pos: Position, to_pos: Position, board: Board) -> bool:
        # Bishop moves diagonally
        dx = abs(to_pos.horizontal - from_pos.horizontal)
        dy = abs(to_pos.vertical - from_pos.vertical)
        
        if dx != dy:
            return False
            
        # Check for pieces in between
        step_x = 1 if to_pos.horizontal > from_pos.horizontal else -1
        step_y = 1 if to_pos.vertical > from_pos.vertical else -1
        
        current_pos = from_pos
        while True:
            current_pos = Position(
                horizontal=chr(current_pos.horizontal + step_x + 64),
                vertical=current_pos.vertical + step_y
            )
            
            if current_pos == to_pos:
                break
                
            if board.get_piece(position=current_pos) is not None:
                return False
                
        return True


class Queen(Piece):
    def __init__(self, *, color: Color, position: Position):
        super().__init__(color=color, position=position)
        self.symbol = 'Q'
        
    def _is_valid_piece_move(self, from_pos: Position, to_pos: Position, board: Board) -> bool:
        # Queen combines Rook and Bishop movement
        dx = abs(to_pos.horizontal - from_pos.horizontal)
        dy = abs(to_pos.vertical - from_pos.vertical)
        
        # Straight line (like Rook)
        is_straight = from_pos.horizontal == to_pos.horizontal or from_pos.vertical == to_pos.vertical
        
        # Diagonal (like Bishop)
        is_diagonal = dx == dy
        
        if not (is_straight or is_diagonal):
            return False
            
        # Check for pieces in between
        step_x = 0
        if from_pos.horizontal < to_pos.horizontal:
            step_x = 1
        elif from_pos.horizontal > to_pos.horizontal:
            step_x = -1
            
        step_y = 0
        if from_pos.vertical < to_pos.vertical:
            step_y = 1
        elif from_pos.vertical > to_pos.vertical:
            step_y = -1
            
        current_pos = from_pos
        while True:
            current_pos = Position(
                horizontal=chr(current_pos.horizontal + step_x + 64),
                vertical=current_pos.vertical + step_y
            )
            
            if current_pos == to_pos:
                break
                
            if board.get_piece(position=current_pos) is not None:
                return False
                
        return True


class King(Piece):
    def __init__(self, *, color: Color, position: Position):
        super().__init__(color=color, position=position)
        self.symbol = 'K'
        
    def _is_valid_piece_move(self, from_pos: Position, to_pos: Position, board: Board) -> bool:
        # King moves one square in any direction
        dx = abs(to_pos.horizontal - from_pos.horizontal)
        dy = abs(to_pos.vertical - from_pos.vertical)
        
        # Regular king move
        if dx <= 1 and dy <= 1:
            # Check if the move would put the king in check
            return not board.would_be_in_check(self.color, to_pos)
            
        # Castling
        if dy == 0 and dx == 2 and not self.has_moved:
            # Determine castling direction and rook position
            king_row = 1 if self.color.name == "WHITE" else 8
            rook_col = 8 if to_pos.horizontal > from_pos.horizontal else 1
            rook_pos = Position(horizontal=chr(rook_col + 64), vertical=king_row)
            
            # Get the rook
            rook = board.get_piece(position=rook_pos)
            
            # Check if it's a valid castling
            if (rook and 
                isinstance(rook, Rook) and 
                not rook.has_moved and 
                not board.is_in_check(self.color)):
                
                # Check if path is clear
                direction = 1 if to_pos.horizontal > from_pos.horizontal else -1
                
                # Check squares in between
                current_pos = from_pos
                while True:
                    current_pos = Position(
                        horizontal=chr(current_pos.horizontal + direction + 64),
                        vertical=current_pos.vertical
                    )
                    
                    if current_pos.horizontal == rook_pos.horizontal:
                        break
                        
                    # Path must be clear
                    if board.get_piece(position=current_pos) is not None:
                        return False
                        
                    # King cannot pass through check
                    if abs(current_pos.horizontal - from_pos.horizontal) <= 2:
                        if board.would_be_in_check(self.color, current_pos):
                            return False
                            
                return True
                
        return False
