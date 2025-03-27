import pygame
import sys
from board import Board
from move import Move
from player import Player
from position import Position
from color import Color
from utils import load_piece_images, pixels_to_position
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, WHITE, BLACK


class TextInputBox:
    def __init__(self, x, y, width, height, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.text = text
        self.font = pygame.font.SysFont('Arial', 28)
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input box
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable
                self.active = True
            else:
                self.active = False
            # Change the color of the input box
            self.color = self.color_active if self.active else self.color_inactive
        
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    return self.text
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    # Add character if it's a printable character (not special keys)
                    if event.unicode.isprintable() and len(self.text) < 20:
                        self.text += event.unicode
                # Re-render the text
                self.txt_surface = self.font.render(self.text, True, self.color)
        return None
    
    def update(self):
        # Resize the box if the text is too long
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width
    
    def draw(self, screen):
        # Draw the text box
        pygame.draw.rect(screen, self.color, self.rect, 2)
        # Draw the text
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))


class Game:
    def __init__(self):
        # Initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Chess Game (Cheese Game)")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 24)
        
        # Load piece images
        load_piece_images()
        
        # Get player names through GUI
        self.player_white, self.player_black = self.get_player_names()
        
        # Initialize game
        self.board = Board(pieces=self.player_white.pieces + self.player_black.pieces)
        self.is_finished = False
        self.player_to_move = self.player_white
        self.winner = None

    def get_player_names(self):
        """Show a screen to enter player names"""
        # Create text input boxes
        white_input = TextInputBox(WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2 - 60, 200, 40)
        black_input = TextInputBox(WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2 + 20, 200, 40)
        
        # Default names in case user skips
        white_name = "Player 1"
        black_name = "Player 2"
        
        # Screen loop
        waiting_for_names = True
        name_screen_step = "white"  # Start with white player
        
        title_font = pygame.font.SysFont('Arial', 36)
        
        while waiting_for_names:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # Handle active input box
                if name_screen_step == "white":
                    result = white_input.handle_event(event)
                    if result is not None:  # Enter was pressed
                        white_name = result if result else white_name
                        name_screen_step = "black"
                elif name_screen_step == "black":
                    result = black_input.handle_event(event)
                    if result is not None:  # Enter was pressed
                        black_name = result if result else black_name
                        waiting_for_names = False
            
            # Update active input box
            if name_screen_step == "white":
                white_input.update()
            else:
                black_input.update()
            
            # Draw screen
            self.screen.fill((240, 240, 240))
            
            # Draw title
            title = title_font.render("CHEESE GAME", True, (50, 50, 50))
            self.screen.blit(title, (WINDOW_WIDTH//2 - title.get_width()//2, 50))
            
            # Draw subtitles
            subtitle = self.font.render("Enter player names and press Enter", True, (80, 80, 80))
            self.screen.blit(subtitle, (WINDOW_WIDTH//2 - subtitle.get_width()//2, 100))
            
            # Draw labels
            white_label = self.font.render("White Player:", True, (50, 50, 50))
            self.screen.blit(white_label, (WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2 - 90))
            
            black_label = self.font.render("Black Player:", True, (50, 50, 50))
            self.screen.blit(black_label, (WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2 - 10))
            
            # Draw active box with highlight
            if name_screen_step == "white":
                pygame.draw.rect(self.screen, (200, 200, 255), 
                                (WINDOW_WIDTH//2 - 110, WINDOW_HEIGHT//2 - 65, 220, 50))
            else:
                pygame.draw.rect(self.screen, (200, 200, 255), 
                                (WINDOW_WIDTH//2 - 110, WINDOW_HEIGHT//2 + 15, 220, 50))
            
            # Draw input boxes
            white_input.draw(self.screen)
            black_input.draw(self.screen)
            
            # Instructions
            instr = self.font.render("Press Enter to continue", True, (80, 80, 80))
            self.screen.blit(instr, (WINDOW_WIDTH//2 - instr.get_width()//2, WINDOW_HEIGHT - 50))
            
            pygame.display.flip()
            self.clock.tick(30)
        
        # Create and return the players
        Color.initialize_colors()
        player_white = Player(name=white_name, color=Color.WHITE)
        player_black = Player(name=black_name, color=Color.BLACK)
        
        return player_white, player_black

    def handle_mouse_click(self, pos):
        """Handle mouse click at given position"""
        x, y = pos
        chess_pos = pixels_to_position(x, y)
        
        # If a piece is already selected, try to move it
        if self.board.selected_piece:
            if chess_pos in self.board.possible_moves:
                # Create and execute the move
                move = Move(
                    from_pos=self.board.selected_pos,
                    to_pos=chess_pos
                )
                
                try:
                    is_checkmate = self.board.do_move(
                        move=move, 
                        player=self.player_to_move
                    )
                    
                    # Switch player turn
                    self.player_to_move = (
                        self.player_black 
                        if self.player_to_move == self.player_white 
                        else self.player_white
                    )
                    
                    # Check for game end conditions
                    if is_checkmate:
                        self.is_finished = True
                        self.winner = self.player_to_move
                    elif self.board.is_stalemate(self.player_to_move.color.name):
                        self.is_finished = True
                        self.winner = None  # Draw
                        
                except ValueError as e:
                    print(f"Invalid move: {e}")
            
            # Clear selection regardless of move success
            self.board.clear_selection()
        else:
            # Try to select a piece
            piece = self.board.get_piece(position=chess_pos)
            if piece and piece.color.name == self.player_to_move.color.name:
                self.board.select_piece(chess_pos)

    def draw(self):
        """Draw the game state"""
        # Fill background
        self.screen.fill(WHITE)
        
        # Draw the board
        self.board.draw(self.screen)
        
        # Display current player's turn
        turn_text = f"Player to move: {self.player_to_move.name} ({self.player_to_move.color.name})"
        text_surface = self.font.render(turn_text, True, BLACK)
        self.screen.blit(text_surface, (10, WINDOW_HEIGHT - 30))
        
        # Display check/checkmate status
        if self.board.is_in_check(self.player_to_move.color.name):
            check_text = "CHECK!"
            text_surface = self.font.render(check_text, True, (255, 0, 0))
            self.screen.blit(text_surface, (WINDOW_WIDTH - 100, WINDOW_HEIGHT - 30))
        
        # Display game over message if finished
        if self.is_finished:
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 128))  # Semi-transparent black
            self.screen.blit(overlay, (0, 0))
            
            if self.winner:
                message = f"Game Over! {self.winner.name} wins!"
            else:
                message = "Game Over! It's a draw!"
                
            text_surface = pygame.font.SysFont('Arial', 36).render(message, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            self.screen.blit(text_surface, text_rect)
            
            # Display restart instructions
            restart_text = "Press 'R' to restart or 'Q' to quit"
            text_surface = self.font.render(restart_text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 40))
            self.screen.blit(text_surface, text_rect)
        
        # Update the display
        pygame.display.flip()

    def start(self):
        """Start the game loop"""
        running = True
        
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
                    if not self.is_finished:
                        self.handle_mouse_click(event.pos)
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # Quit
                        running = False
                    elif event.key == pygame.K_r and self.is_finished:  # Restart
                        # Reset game
                        self.__init__()
            
            # Draw the game
            self.draw()
            
            # Cap the frame rate
            self.clock.tick(60)
        
        # Clean up
        pygame.quit()
