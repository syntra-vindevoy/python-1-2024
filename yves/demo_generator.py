
import timeit
import tracemalloc
from pathlib import Path


def generate_large_file(filename, num_lines):
    from lorem import sentence

    with open(filename, "w") as f:
        for _ in range(num_lines):
            f.write(sentence() + "\n")


# Function to measure memory usage
def measure(func, times=1, *args):
    method = args[0]

    tracemalloc.start()
    execution_time = timeit.timeit(lambda: func(method=method), setup="from __main__ import read", number=times)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    current_mb = current / 1024 / 1024
    peak_mb = peak / 1024 / 1024

    return method, execution_time, current_mb, peak_mb


def read_file(path):
    with open(path, "r") as f:
        lines = f.readlines()

        return lines


def read_yield(path):
    with open(path, "r") as f:
        for line in f:
            yield line


def read(method: int):
    path = Path(__file__).parent.joinpath("lorem.txt").resolve()

    if method == 1:
        lines = read_file(path)
    else:
        lines = read_yield(path)

    total_lines = 0
    vowel_lines = 0

    for line in lines:
        total_lines += 1

        if line.strip()[:1].upper() in "AEIOUY":
            vowel_lines += 1

    print(
        "Method:",
        "NORMAL" if method == 1 else "YIELD ",
        "- File",
        path,
        "has",
        vowel_lines,
        "lines starting with a vowel on a total of",
        total_lines,
        "lines:",
        vowel_lines * 100 // total_lines,
        "%",
        )


def main():
    times = 5

    method_1, execution_time_1, current_mb_1, peak_mb_1 = measure(read, times, 1)
    method_2, execution_time_2, current_mb_2, peak_mb_2 = measure(read, times, 2)

    print("\nNORMAL READ" if method_1 == 1 else "YIELD READ")
    print(f"  - Average execution time over {times} runs: {execution_time_1 / times:.5f} seconds")
    print(f"  - Current memory usage: {current_mb_1:.5f} MB")
    print(f"  - Peak memory usage: {peak_mb_1:.5f} MB\n")

    print("\nNORMAL READ" if method_2 == 1 else "YIELD READ")
    print(f"  - Average execution time over {times} runs: {execution_time_2 / times:.5f} seconds")
    print(f"  - Current memory usage: {current_mb_2:.5f} MB")
    print(f"  - Peak memory usage: {peak_mb_2:.5f} MB\n")



if __name__ == "__main__":
    main()

# if __name__ == "__main__":
#     number_of_lines = 2 * 1000 * 1000
#
#     output_file = Path(__file__).parent.joinpath("lorem.txt").resolve()
#     generate_large_file(output_file, number_of_lines)
#     print(f"File '{output_file}' with {number_of_lines} lines was successfully created.")
#

