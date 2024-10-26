def crossing_time():
    # Crossing times for each man
    A = 1
    B = 2
    C = 5
    D = 10

    # Step by step optimized process
    total_time = 0

    # A and B cross -> A returns -> C and D cross -> B returns -> A and B cross
    total_time += 2  # A and B cross (2 mins)
    print("Step 1: A and B cross (2 mins), total =", total_time, "mins")

    total_time += 1  # A returns with the flashlight (1 min)
    print("Step 2: A returns (1 min), total =", total_time, "mins")

    total_time += 10  # C and D cross (10 mins)
    print("Step 3: C and D cross (10 mins), total =", total_time, "mins")

    total_time += 2  # B returns with the flashlight (2 mins)
    print("Step 4: B returns (2 mins), total =", total_time, "mins")

    total_time += 2  # A and B cross again (2 mins)
    print("Step 5: A and B cross again (2 mins), total =", total_time, "mins")

    return total_time


# Calculate the total crossing time
total_crossing_time = crossing_time()
print("Total time for all to cross the river:", total_crossing_time, "minutes")
