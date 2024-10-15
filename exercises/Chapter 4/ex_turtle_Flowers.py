import math
from turtle import Turtle, done

# Create a turtle object
bob = Turtle()

# Function to draw a polyline
def polyline(n, length, angle):
    for _ in range(n):
        bob.forward(length)
        bob.left(angle)

# Function to draw an arc
def arc(radius, angle):
    arc_length = 2 * math.pi * radius * angle / 360  # Calculate the arc length
    n = 100                                         # Number of segments for smoothness
    length = arc_length / n                         # Length of each segment
    step_angle = angle / n                          # Angle between each segment
    polyline(n, length, step_angle)                 # Draw the arc using polyline

# Function to draw a petal using two arcs
def petal(radius, angle):
    arc(radius, angle)       # Draw the first arc
    bob.left(180 - angle)    # Turn to position for the second arc
    arc(radius, angle)       # Draw the second arc
    bob.left(180 - angle)    # Reposition turtle for the next petal

# Function to draw a flower with multiple petals
def flower(num_petals, radius, angle):
    for _ in range(num_petals):
        petal(radius, angle)        # Draw a single petal
        bob.left(360 / num_petals)  # Rotate turtle to position for next petal

# Example usage
flower(12, 100, 60)  # Draw a flower with 6 petals, radius of 100, and angle of 60 degrees

# Keep the window open until closed manually
done()
