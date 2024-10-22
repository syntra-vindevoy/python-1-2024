def draw_grid(rows, cols):
    # Calculate the number of cells and the size of each cell
    cell_height = 3
    cell_width = 5

    # Draw the top border
    for r in range(rows):
        print("+", end="")
        print("-" * cell_width, end="")
    print("+")

    # Draw the rows of the grid
    for r in range(cell_height):
        for c in range(cols):
            print("|", end=" " * cell_width)
        print("|")

    # Draw the bottom border of the last row
    for r in range(rows):
        print("+", end="")
        print("-" * cell_width, end="")
    print("+")


# Example usage
draw_grid(2, 2)  # Adjust the numbers for more rows/columns


