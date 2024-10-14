import turtle


def draw_petal(turtle, radius, angle):
    """Draws a single petal."""
    turtle.circle(radius, angle)
    turtle.left(180 - angle)
    turtle.circle(radius, angle)
    turtle.left(180 - angle)


def draw_flower(t, num_petals, radius):
    """Draws a flower with a specified number of petals, radius, and angle for each petal."""
    petal_angle = 360 / num_petals
    angle = 360 / num_petals
    for _ in range(num_petals):
        draw_petal(t, radius, angle)
        t.left(petal_angle)


def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Flower Drawing with Turtle")

    # Create the turtle
    flower_turtle = turtle.Turtle()
    flower_turtle.speed(10)

    # Draw the flower
    draw_flower(flower_turtle, num_petals=12, radius=300)  # Fixed the argument order

    # Hide the turtle and display the window
    flower_turtle.hideturtle()

    # Wait for a mouse click or window close event
    screen.mainloop()


if __name__ == "__main__":
    main()
