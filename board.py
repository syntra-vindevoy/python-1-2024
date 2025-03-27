import pygame
from typing import Optional, Dict, List, Tuple

from move import Move
from player import Player
from position import Position
from piece import Piece, King, Rook
from constants import SQUARE_SIZE, LIGHT_SQUARE, DARK_SQUARE, HIGHLIGHT, MOVE_HINT, WINDOW_HEIGHT, WINDOW_WIDTH
from utils import position_to_pixels


class Board:
    def __init__(self, *, pieces: list):
        self.pieces = pieces
        self.positions: Dict[Position, Piece] = {}
        self.captured_pieces: List[Piece] = []
        self.selected_piece: Optional[Piece] = None
        self.selected_pos: Optional[Position] = None
        self.possible_moves: List[Position] = []
        self.last_move: Optional[Tuple[Position, Position]] = None
        self.setup()

    def setup(self):
        """Place all pieces in their starting positions"""
        self.positions.clear()
        for piece in self.pieces:
            if not piece.captured:
                self.positions[piece.position] = piece

    def do_move(self, *, move: Move, player: Player) -> bool:
        """Execute a move if it's valid"""
        piece = self.get_piece(position=move.from_pos)

        if piece is None:
            raise ValueError(f"There is no piece on {move.from_pos}")

        if piece.color != player.color:
            raise ValueError("On the from position is a piece of the other player")

        if not piece.valid_move(move.from_pos, move.to_pos, self):
            raise ValueError(f"You cannot move from {move.from_pos} to {move.to_pos}")
            
        # Handle en passant capture
        en_passant_pos = None
        if isinstance(piece, Piece) and piece.__class__.__name__ == "Pawn":
            # If pawn is moving diagonally to an empty square, it's en passant
            if (move.from_pos.horizontal != move.to_pos.horizontal and 
                self.get_piece(position=move.to_pos) is None):
                en_passant_pos = Position(
                    horizontal=chr(move.to_pos.horizontal + 64),
                    vertical=move.from_pos.vertical
                )
        
        # Execute the move
        self._execute_move(piece, move.from_pos, move.to_pos)
        
        # Handle special en passant capture
        if en_passant_pos:
            captured = self.get_piece(position=en_passant_pos)
            if captured:
                captured.captured = True
                self.captured_pieces.append(captured)
                del self.positions[en_passant_pos]
        
        # Handle castling
        if isinstance(piece, King) and abs(move.to_pos.horizontal - move.from_pos.horizontal) == 2:
            # Determine castling direction and rook positions
            king_row = move.from_pos.vertical
            is_kingside = move.to_pos.horizontal > move.from_pos.horizontal
            
            rook_from_col = 8 if is_kingside else 1
            rook_to_col = 6 if is_kingside else 4
            
            rook_from_pos = Position(horizontal=chr(rook_from_col + 64), vertical=king_row)
            rook_to_pos = Position(horizontal=chr(rook_to_col + 64), vertical=king_row)
            
            rook = self.get_piece(position=rook_from_pos)
            if rook:
                self._execute_move(rook, rook_from_pos, rook_to_pos)
        
        # Reset en passant vulnerability for all pawns of the current player
        for p in player.pieces:
            if p.__class__.__name__ == "Pawn":
                p.en_passant_vulnerable = False
        
        # Store last move for highlighting
        self.last_move = (move.from_pos, move.to_pos)
        
        # Return whether the opponent is in checkmate
        return self.is_checkmate(player.color)

    def _execute_move(self, piece: Piece, from_pos: Position, to_pos: Position):
        """Execute the physical movement of a piece"""
        # Handle capture
        target = self.get_piece(position=to_pos)
        if target:
            target.captured = True
            self.captured_pieces.append(target)
        
        # Update piece position
        piece.move_to(to_pos)
        
        # Update board positions dictionary
        del self.positions[from_pos]
        self.positions[to_pos] = piece

    def get_piece(self, *, position: Position) -> Optional[Piece]:
        """Get piece at the specified position or None if empty"""
        return self.positions.get(position)

    def is_in_check(self, color: str) -> bool:
        """Check if the player with the given color is in check"""
        # Find the king
        king = None
        for piece in self.pieces:
            if (piece.__class__.__name__ == "King" and 
                piece.color.name == color and 
                not piece.captured):
                king = piece
                break
        
        if not king:
            return False  # No king found (shouldn't happen in normal chess)
        
        # Check if any opponent piece can attack the king
        for piece in self.pieces:
            if piece.color.name != color and not piece.captured:
                if piece.valid_move(piece.position, king.position, self):
                    return True
        
        return False

    def would_be_in_check(self, color: str, king_pos: Position) -> bool:
        """Check if the king would be in check after moving to king_pos"""
        # Find the king
        king = None
        for piece in self.pieces:
            if (piece.__class__.__name__ == "King" and 
                piece.color.name == color and 
                not piece.captured):
                king = piece
                break
        
        if not king:
            return False
        
        # Temporarily move the king
        old_pos = king.position
        
        # Create a temporary copy of the positions dict to restore later
        temp_positions = self.positions.copy()
        
        # Update positions as if the king moved
        if old_pos in self.positions:
            del self.positions[old_pos]
        self.positions[king_pos] = king
        
        # Temporarily update king position
        king.position = king_pos
        
        # Check if any opponent piece can attack the king
        in_check = False
        for piece in self.pieces:
            if piece.color.name != color and not piece.captured:
                if piece._is_valid_piece_move(piece.position, king_pos, self):
                    in_check = True
                    break
        
        # Restore the king's position and board state
        king.position = old_pos
        self.positions = temp_positions
        
        return in_check

    def is_checkmate(self, opponent_color: str) -> bool:
        """Check if the opponent is in checkmate"""
        # Determine the color of the player to check for checkmate
        color = "WHITE" if opponent_color == "BLACK" else "BLACK"
        
        # If not in check, can't be checkmate
        if not self.is_in_check(color):
            return False
        
        # Check if any move can get out of check
        for piece in self.pieces:
            if piece.color.name == color and not piece.captured:
                possible_moves = piece.get_possible_moves(self)
                if possible_moves:
                    return False
        
        # No legal moves and in check = checkmate
        return True

    def is_stalemate(self, color: str) -> bool:
        """Check if the player with the given color is in stalemate"""
        # If in check, it's not stalemate
        if self.is_in_check(color):
            return False
        
        # Check if any piece has legal moves
        for piece in self.pieces:
            if piece.color.name == color and not piece.captured:
                possible_moves = piece.get_possible_moves(self)
                if possible_moves:
                    return False
        
        # No legal moves and not in check = stalemate
        return True

    def select_piece(self, position: Position) -> bool:
        """Select a piece at the given position"""
        piece = self.get_piece(position=position)
        
        if piece:
            self.selected_piece = piece
            self.selected_pos = position
            self.possible_moves = piece.get_possible_moves(self)
            return True
        
        return False

    def clear_selection(self):
        """Clear the current selection"""
        self.selected_piece = None
        self.selected_pos = None
        self.possible_moves = []

    def draw(self, surface: pygame.Surface):
        """Draw the chess board and pieces"""
        # Draw board squares
        for row in range(8):
            for col in range(8):
                # Calculate rectangle position and size
                rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                
                # Determine square color
                if (row + col) % 2 == 0:
                    color = LIGHT_SQUARE
                else:
                    color = DARK_SQUARE
                
                # Draw the square
                pygame.draw.rect(surface, color, rect)
                
                # Draw position
                pos = Position(horizontal=chr(col + 65), vertical=8 - row)
                
                # Draw last move highlight
                if self.last_move and (pos == self.last_move[0] or pos == self.last_move[1]):
                    highlight_rect = pygame.Rect(
                        col * SQUARE_SIZE + 4, 
                        row * SQUARE_SIZE + 4, 
                        SQUARE_SIZE - 8, 
                        SQUARE_SIZE - 8
                    )
                    pygame.draw.rect(surface, HIGHLIGHT, highlight_rect, 3)
                
                # Draw selected square
                if self.selected_pos and pos == self.selected_pos:
                    pygame.draw.rect(surface, HIGHLIGHT, rect, 4)
                
                # Draw possible move indicator
                if pos in self.possible_moves:
                    pygame.draw.circle(
                        surface, 
                        MOVE_HINT, 
                        (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 
                        SQUARE_SIZE // 6
                    )
        
        # Draw rank and file labels
        font = pygame.font.SysFont('Arial', 16)
        for i in range(8):
            # Draw file labels (A-H)
            file_label = chr(65 + i)
            text = font.render(file_label, True, (0, 0, 0))
            surface.blit(text, (i * SQUARE_SIZE + 5, WINDOW_HEIGHT - 20))
            
            # Draw rank labels (1-8)
            rank_label = str(8 - i)
            text = font.render(rank_label, True, (0, 0, 0))
            surface.blit(text, (5, i * SQUARE_SIZE + 5))
        
        # Draw pieces
        for piece in self.pieces:
            if not piece.captured:
                piece.draw(surface)
