def bottle_line(count):
    """Return the appropriate line for the number of bottles."""
    if count == 0:
        return "No more bottles of beer on the wall."
    elif count == 1:
        return "1 bottle of beer on the wall."
    else:
        return f"{count} bottles of beer on the wall."

def bottle_verse(starting_bottles):
    """Print the verse starting from the given number of bottles."""
    if starting_bottles > 0:
        first_line = bottle_line(starting_bottles)
        second_line = bottle_line(starting_bottles)

        print(first_line)
        print(second_line.replace("on the wall", ""))  # Remove "on the wall" from the second line
        print("Take one down, pass it around")

        next_bottle_count = starting_bottles - 1
        next_line = bottle_line(next_bottle_count)
        print(next_line)
    else:
        print(bottle_line(starting_bottles))  # Print the final line when there are no bottles
        print("Go to the store and buy some more.")

    print()  # Add an empty line for spacing

def sing_song():
    """Sing the entire song from 99 bottles down to 0."""
    for bottles in range(99, -1, -1):
        bottle_verse(bottles)

# Call the function to sing the entire song
sing_song()
