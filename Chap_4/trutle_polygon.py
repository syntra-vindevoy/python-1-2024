import turtle
import math


def draw_polygon(t, sides, size):
    """Draws a regular polygon with the given number of sides and size."""
    angle = 360 / sides
    vertices = []
    for _ in range(sides):
        vertices.append(t.pos())
        t.forward(size)
        t.left(angle)
    return vertices


def draw_diagonals(t, vertices):
    """Draws diagonals connecting each vertex to the center of the polygon."""
    center_x = sum(v[0] for v in vertices) / len(vertices)
    center_y = sum(v[1] for v in vertices) / len(vertices)
    t.penup()
    t.goto(center_x, center_y)
    t.pendown()
    for vertex in vertices:
        t.goto(vertex)
        t.goto(center_x, center_y)


def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Polygon Divided by Triangles with Turtle")

    # Create the turtle
    polygon_turtle = turtle.Turtle()
    polygon_turtle.speed(5)

    # Parameters for the polygon
    sides = 12  # Number of sides of the polygon
    size = 100  # Length of each side of the polygon

    # Draw the polygon and get the vertices
    vertices = draw_polygon(polygon_turtle, sides, size)

    # Draw diagonals to divide the polygon into triangles
    draw_diagonals(polygon_turtle, vertices)

    # Hide the turtle and display the window
    polygon_turtle.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    main()
