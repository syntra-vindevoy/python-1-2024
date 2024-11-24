# https://www.youtube.com/watch?v=gNA5BQ7B5YU&t=59s

'''
tell me about surfaces in pygame


Pygame Surfaces: The Canvas of Your Game

In Pygame, a Surface is essentially a rectangular block of pixels that serves as the foundation for displaying graphics. It's like a blank canvas onto which you can draw shapes, text, and images.

Key Concepts:

Creation:
You create a Surface using the pygame.Surface() function:

#Python
import pygame

# Create a surface of size 800x600 pixels
screen = pygame.display.set_mode((800, 600))

Drawing:
You can draw on a Surface using various functions provided by Pygame:
pygame.draw.rect(): Draws rectangles
pygame.draw.circle(): Draws circles
pygame.draw.line(): Draws lines
pygame.draw.polygon(): Draws polygons
You can also fill a Surface with a color using fill():

Python

screen.fill((255, 0, 0))  # Fill the screen with red


Blitting:
Blitting is the process of copying one Surface onto another. It's often used to draw images or other Surfaces onto the main screen:
Python
# Load an image
image = pygame.image.load("image.png")

# Blit the image onto the screen
screen.blit(image, (100, 100))
Wees voorzichtig met code.

Transparency:
You can control the transparency of Surfaces using colorkeying or alpha values:
Colorkeying: Sets a specific color to be transparent:
Python
image.set_colorkey((255, 0, 255))  # Make magenta color transparent
Wees voorzichtig met code.

Alpha Values: Controls the overall transparency of the Surface:
Python
image.set_alpha(128)  # 50% transparency
Wees voorzichtig met code.

Common Use Cases:

Game Screens: The main game screen is often represented by a Surface.
Sprites: Individual game objects like characters, enemies, and items can be represented as Surfaces.
Backgrounds: Background images or tilesets can be loaded as Surfaces.
Text Rendering: Text can be rendered onto a Surface using fonts.
UI Elements: Buttons, menus, and other UI elements can be created using Surfaces.
By understanding and effectively using Surfaces, you can create visually appealing and interactive games with Pygame.
'''