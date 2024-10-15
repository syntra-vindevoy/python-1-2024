import turtle

def triangle(t, side_length):
    # Draw a triangle slice
    for _ in range(3):
        t.forward(side_length)  # Draw one side
        t.left(120)              # Turn to draw the next side of the triangle

def draw_polygon_from_triangles(side_length, num_sides):
    t = turtle.Turtle()

    # Number of triangles to draw
    num_triangles = num_sides  # The number of sides equals the number of triangles

    # Angle to turn after each triangle
    angle = 360 / num_triangles

    # Draw the polygon using triangles
    for _ in range(num_triangles):
        triangle(t, side_length)   # Draw one triangle
        t.left(angle)              # Rotate to position for the next triangle

    t.hideturtle()
    turtle.done()

# Example usage: Draw a hexagon made of 6 triangles with side length 100
draw_polygon_from_triangles(120, 8)

# You can also draw other shapes:
# draw_polygon_from_triangles(100, 3)  # Triangle
# draw_polygon_from_triangles(100, 4)  # Square
# draw_polygon_from_triangles(100, 5)  # Pentagon
