from itertools import combinations  # Import combinations function to generate pairs

solutions = {}  # Dictionary to store solutions with total times as keys

def solve(left, right, total_time, crossings):  # Recursive function to solve the problem
    global solutions  # Access the global solutions dictionary

    couples = list(combinations(left, 2))  # Generate all pairs of people on the left side

    b_left, b_right, b_total_time, b_crossings = left.copy(), right.copy(), total_time, crossings.copy()  # Backup the current state

    for couple in couples.copy():  # Iterate over each pair of people
        left, right, total_time, crossings = b_left.copy(), b_right.copy(), b_total_time, b_crossings.copy()  # Restore the backed-up state

        right.extend(couple)  # Move the pair to the right side
        left.remove(couple[0])  # Remove the first person of the pair from the left side
        left.remove(couple[1])  # Remove the second person of the pair from the left side

        total_time += max(couple)  # Add the crossing time (the slower person's time)
        crossings.append(  # Log the crossing
            f"{couple[0]} and {couple[1]} cross the bridge in {max(couple)} seconds.  Left: {left}, Right: {right}.  Total time: {total_time}")

        if len(right) == 4:  # If all 4 people are on the right side
            if total_time in solutions:  # Check if this time is already in solutions
                solutions[total_time].append(crossings)  # Add the current solution to the list
            else:
                solutions[total_time] = [crossings]  # Create a new entry for this time

        else:  # If not all people have crossed
            c_left, c_right, c_total_time, c_crossings = left.copy(), right.copy(), total_time, crossings.copy()  # Backup the current state again

            for p in right.copy():  # Iterate over each person on the right
                left, right, total_time, crossings = c_left.copy(), c_right.copy(), c_total_time, c_crossings.copy()  # Restore the state

                left.append(p)  # Move the person back to the left side
                right.remove(p)  # Remove the person from the right side

                total_time += p  # Add the return time (the person's time)
                crossings.append(  # Log the return
                    f"{p} goes back in {p} seconds.  Left: {left}, Right: {right}.  Total time: {total_time}")

                solve(left.copy(), right.copy(), total_time, crossings.copy())  # Recurse with the updated state

def main():  # Main function to start the process
    global solutions  # Access the global solutions dictionary

    left = [1, 2, 5, 10]  # Initial list of people on the left
    right = []  # Initial empty list for people on the right

    solve(left, right, 0, [])  # Call the solve function with the initial state

    solutions = dict(sorted(solutions.items(), key=lambda item: item[0]))  # Sort solutions by total time

    print("\nAll solutions:")
    for solution in solutions:  # Iterate over each total time in the solutions
        print(f"Solutions in {solution} seconds:")  # Print the total time

        cr_counter = 0  # Initialize a crossing counter
        for crossing in solutions[solution]:  # Iterate over each crossing sequence
            cr_counter += 1  # Increment the crossing counter
            print(f"Cross {cr_counter}:", crossing)  # Print the crossing sequence

    # Print the fastest solution
    fastest_time = min(solutions.keys())  # Find the smallest key (fastest time)
    print("\nFastest solution:")
    print(f"In {fastest_time} seconds:")
    for crossing in solutions[fastest_time]:  # Iterate over the fastest crossing sequence
        print(crossing)


if __name__ == "__main__":  # Entry point of the script
    main()  # Call the main function

