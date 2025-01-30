#https://leetcode.com/problems/two-sum/description/

def two_sum(nums, target):
    # Create a hashmap to store the numbers and their indices
    num_indices = {}

    for i, num in enumerate(nums):
        # Calculate the complement
        complement = target - num

        # Check if the complement exists in the hashmap
        if complement in num_indices:
            # If found, return the indices
            return [num_indices[complement], i]

        # Otherwise, store the current number's index
        num_indices[num] = i

    # If no solution is found, return an empty list (not expected in the problem)
    return []

nums = [3, 2, 4, 9, 1, 7]
target = 10
print(two_sum(nums, target))  # Output: [0, 1]


# Input: nums = [3,2,4], target = 6
# Output: [1,2]