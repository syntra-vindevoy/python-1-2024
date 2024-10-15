import turtle
import math

# Function to draw a polyline
def polyline(n, length, angle):
    """Draws n line segments with given length and angle between them."""
    for _ in range(n):
        turtle.forward(length)  # Move forward by the given length
        turtle.left(angle)      # Turn left by the given angle

# Function to draw an arc
def arc(radius, angle):
    """Draws an arc with the given radius and angle."""
    arc_length = 2 * math.pi * radius * angle / 360  # Calculate the total arc length
    n = 100                                          # Number of segments (higher value gives a smoother curve)
    length = arc_length / n                         # Length of each segment
    step_angle = angle / n                          # Angle between each segment
    polyline(n, length, step_angle)                 # Draw the polyline approximation of the arc

# Example usage
turtle.speed(1)  # Slow down the turtle for better visualization
arc(80, 100)    # Draw an arc with radius 100 and 180 degrees (a semicircle)

# Keep the window open until clicked
turtle.done()
