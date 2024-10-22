def print_n_times(string, n):
    if n > 0:
        print(string)
        print_n_times(string, n-1)