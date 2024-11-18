def main():
    weights = {}  # Use a regular dictionary
    stones = [1, 3, 9, 27]  # List of stone values

    for stone in stones:  # Loop through each stone in the list
        # Make a list of current keys and sort them
        keys = sorted(weights.keys())  # Get the keys from 'weights' and sort them
        for p in keys:  # Loop through each key in the sorted list
            weights[stone + p] = [p, stone]  # Add new entry for stone + p
            weights[stone - p] = [-p, stone]  # Add new entry for stone - p

        weights[stone] = [stone]  # Add the stone itself to the dictionary with its own value

    # To print in sorted order, we sort the keys of the dictionary
    sorted_weights = {k: weights[k] for k in sorted(weights)}  # Sort the dictionary by keys
    print(sorted_weights)  # Print the sorted dictionary

main()  # Call the main function to execute
