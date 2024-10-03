def draw_grid(columns, rows, box_size):
    def draw_horizontal_border():
        print(('+ ' + '- ' * box_size) * columns + '+')

    def draw_vertical_borders():
        for _ in range(box_size):
            print(('| ' + ' ' * (box_size * 2) + ' |') * columns + '|')

    # Draw the grid
    for _ in range(rows):
        draw_horizontal_border()
        draw_vertical_borders()
    # Draw the final bottom border
    draw_horizontal_border()


# Example usage
draw_grid(2, 2, 4)  # 2 columns, 2 rows, box size 4
draw_grid(3, 3, 2)  # 3 columns, 3 rows, box size 2
