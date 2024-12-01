
def triangle(base, height):
    """Calculates the area of a triangle"""
    return (base * height) / 2


def rectangle(base, height):
    """Calculates the area of a rectangle"""
    return base * height


def combined_area(base, height):
    """Calculates the combined area of a triangle and rectangle with the same base and height"""
    triangle_area = triangle(base, height)
    rectangle_area = rectangle(base, height)
    return triangle_area + rectangle_area


print(combined_area(1, 16))


def parabola_segment_area(base, height, segments):
    segment_width = base / segments
    total_area = 0.0

    for i in range(segments):
        # Calculate the x coordinates at the edges of the segment
        x_start = i * segment_width
        x_end = (i + 1) * segment_width
        # Calculate the height of the parabola at these x coordinates
        y_start = height * ((x_start / base) ** 2)
        y_end = height * ((x_end / base) ** 2)

        trapezoid_area = (y_start + y_end) / 2 * segment_width
        total_area += trapezoid_area

    return total_area


def refine_parabola_area(base, height):
    """Refines the parabola area calculation until it reaches 4 decimal precision."""
    segments = 1  # Start with one segment
    previous_area = 0
    precision = 0.0001  # Target precision
    while True:
        current_area = parabola_segment_area(base, height, segments)
        if abs(current_area - previous_area) < precision:
            break
        previous_area = current_area
        segments *= 2  # Double the number of segments for higher accuracy
    return current_area


# Example usage:
base = 4
height = 16
area = refine_parabola_area(base, height)
print(f"Refined area under the parabola: {area}")