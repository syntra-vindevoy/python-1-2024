

import tkinter as tk
import pygame

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Create a Tkinter window
root = tk.Tk()
root.title("Tkinter-Pygame Integration")

# Create a Tkinter button
button = tk.Button(root, text="Start Game", command=lambda: start_game())
button.pack()

# Function to start the game
def start_game():
    # Pygame game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with a color
        screen.fill((0, 0, 255))

        # Update the display
        pygame.display.flip()

# Start the Tkinter event loop
root.mainloop()

# Quit Pygame when the Tkinter window is closed
pygame.quit()