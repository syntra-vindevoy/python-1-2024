import tkinter as tk
import pygame
import os
import sys

# Initialize Tkinter
root = tk.Tk()
root.title("Pygame in Tkinter")

# Set up the frame for embedding Pygame
embed = tk.Frame(root, width=800, height=600)
embed.pack()

# Add a button to the Tkinter window
def on_button_click():
    print("Button clicked!")

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

# Ensure the Tkinter window is fully initialized
root.update()

# Set the SDL_WINDOWID environment variable
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'x11'  # Use 'x11' driver for Linux

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Set up the font for rendering text
font = pygame.font.SysFont(None, 55)
text_surface = font.render('Hello, World!', True, (255, 255, 255))

# Function to update the Pygame display
def update_pygame():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            root.quit()
            sys.exit()

    screen.fill((0, 0, 255))  # Fill the screen with blue
    screen.blit(text_surface, (200, 250))  # Draw the text surface
    pygame.display.flip()  # Update the display

    root.after(10, update_pygame)  # Schedule the next update

# Start the Pygame update loop
update_pygame()

# Start the Tkinter event loop
root.mainloop()