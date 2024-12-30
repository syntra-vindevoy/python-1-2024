import pickle
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
cache_file = os.path.join(script_dir, 'memo_cache.pkl')

# Function to save memoization dictionary to a pickle file
def save_memo(cache, filename=cache_file):
    with open(filename, 'wb') as f:
        pickle.dump(cache, f)

# Function to load memoization dictionary from a pickle file
def load_memo(filename=cache_file):
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}

# Example memoized function
def memoized_function(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        memo[n] = n
    else:
        memo[n] = memoized_function(n-1, memo) + memoized_function(n-2, memo)
    return memo[n]

# Load memoization cache
memo_cache = load_memo()

# Use the memoized function
result = memoized_function(10, memo_cache)

# Save the updated memoization cache
save_memo(memo_cache)

print(result)