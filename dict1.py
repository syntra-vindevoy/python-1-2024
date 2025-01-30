# from time import perf_counter
#
# # Precompute a lookup table to convert ASCII values to bitmasks for a-z
# # Each lowercase letter (a-z) is mapped to a unique bit in a 32-bit integer
# # Example: 'a' → 0b0001, 'b' → 0b0010, ..., 'z' → 0b10000000000000000000000000
# LOOKUP = [(1 << (c - 97)) if 97 <= c <= 122 else 0 for c in range(256)]
#
# def find_combination():
#     # Read the file as raw bytes and convert to lowercase for uniformity
#     with open("words(1).txt", "rb") as f:
#         data = f.read().lower()
#
#     # Initialize frequency counter for each letter (a-z)
#     freq = [0] * 26
#
#     # Store bitmask representations of all words
#     masks = []
#
#     # Current bitmask for the word being processed
#     current_mask = 0
#
#     # Process each byte in the file (O(n) time complexity)
#     for c in data:
#         if c == 10:  # Newline character indicates end of a word
#             if current_mask:
#                 masks.append(current_mask)
#                 current_mask = 0  # Reset for the next word
#             continue
#
#         # Convert character to precomputed bitmask
#         bit = LOOKUP[c]
#
#         # Check if the character is a valid lowercase letter and not already in the mask
#         if bit and not (current_mask & bit):
#             freq[c - 97] += 1  # Increment frequency counter
#             current_mask |= bit  # Add the character to the current word's mask
#
#     # Add the last word if the file doesn't end with a newline
#     if current_mask:
#         masks.append(current_mask)
#
#     # Select the 5 least frequent characters using sorted indices
#     selected = sorted(range(26), key=lambda x: freq[x])[:5]
#
#     # Create a combined exclusion mask for the selected characters
#     exclusion = sum(1 << x for x in selected)
#
#     # Count words that do NOT contain any of the selected characters
#     count = sum(1 for mask in masks if not (mask & exclusion))
#
#     # Convert indices to actual characters (a-z)
#     return [chr(x + 97) for x in selected], count
#
# if __name__ == "__main__":
#     # Precision timing for performance measurement
#     start = perf_counter()
#     combo, count = find_combination()
#     duration = perf_counter() - start
#
#     # Print results with microsecond-level timing
#     print(f"{count} results | Combination: {combo} | Time: {duration:.6f}s")




# Import required libraries
import numpy as np
from numba import njit, prange  # For JIT compilation and parallel processing
import time

# Precompute bitmask array for ASCII characters 0-127
# Creates a 32-bit mask for valid lowercase letters (97-122 = a-z)
BITMASK = np.array([(1 << (c - 97)) if 97 <= c <= 122 else 0
                    for c in range(128)], dtype=np.uint32)


# Numba-optimized function for parallel mask computation
@njit(nogil=True, parallel=True, fastmath=True)
def compute_masks(data, starts, ends):
    """
    Compute bitmask representations for words in parallel.
    Each bit in the 32-bit mask represents a unique letter (a-z).
    """
    masks = np.zeros(len(starts), dtype=np.uint32)
    # Parallel loop over all words using prange
    for i in prange(len(starts)):
        unique = 0  # Initialize bitmask for current word
        ptr = starts[i]
        # Process characters until word end
        while ptr < ends[i]:
            c = data[ptr]
            if 97 <= c <= 122:  # Only process valid lowercase letters
                unique |= BITMASK[c]  # Set corresponding bit
            ptr += 1
        masks[i] = unique  # Store final mask for this word
    return masks


def find_combination():
    """Main processing function to find optimal character combination."""
    # Load and preprocess data
    with open("words(1).txt", "rb") as f:
        buf = f.read()  # Read entire file as bytes

    # Convert to numpy array and filter characters
    raw = np.frombuffer(buf, dtype=np.uint8)  # Direct buffer access
    # Create boolean mask for valid characters (newlines and a-z)
    mask = (raw == 10) | ((raw >= 97) & (raw <= 122))
    filtered = raw[mask]  # Apply character filter

    # Find word boundaries using newline positions
    newlines = np.where(filtered == 10)[0]
    num_words = len(newlines) + 1  # Calculate total words

    # Initialize arrays for word boundaries
    starts = np.empty(num_words, dtype=np.int64)
    ends = np.empty(num_words, dtype=np.int64)

    # Set start/end positions for each word
    starts[0] = 0  # First word starts at 0
    if newlines.size > 0:
        starts[1:] = newlines + 1  # Subsequent starts after newlines
        ends[:-1] = newlines  # Ends at newline positions
    ends[-1] = len(filtered)  # Last word ends at array end

    # Filter out empty words (zero-length)
    valid_words = (ends - starts) > 0
    starts = starts[valid_words]
    ends = ends[valid_words]

    # Compute character masks using JIT-optimized function
    masks = compute_masks(filtered, starts, ends)

    # Calculate character frequencies using bitwise operations
    freq = np.zeros(26, dtype=np.uint32)
    for c in prange(26):  # Parallel loop over all letters
        freq[c] = np.count_nonzero(masks & (1 << c))

    # Select 5 rarest characters using partial sorting
    selected = np.argpartition(freq, 5)[:5]
    selected = selected[np.argsort(freq[selected])]  # Sort selected subset

    # Create exclusion mask from selected characters
    exclusion = np.uint32(sum(1 << c for c in selected))
    # Count words without any excluded characters
    remaining = np.count_nonzero((masks & exclusion) == 0)

    return [chr(c + 97) for c in selected], remaining


if __name__ == "__main__":
    # Warmup JIT compiler to exclude compilation time from measurements
    compute_masks(np.array([97, 98, 99], dtype=np.uint8),
                  np.array([0], dtype=np.int64),
                  np.array([3], dtype=np.int64))

    # Precision timing measurement
    t0 = time.perf_counter_ns()
    combo, count = find_combination()
    t1 = time.perf_counter_ns()

    # Print formatted results
    print(f"Results: {count} | Chars: {combo} | Time: {(t1 - t0) / 1e9:.6f}s")