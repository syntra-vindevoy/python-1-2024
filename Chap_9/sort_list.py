from datetime import datetime


import random

# Generate a list of 100 random integers between 1 and 1000
random_numbers = [random.randint(1, 1000) for _ in range(100)]

# Example usage

print(f"test array: {random_numbers}")


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choosing the middle element as the pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)


# Example usage
arr = random_numbers
sorted_arr = quicksort(arr)
print(f"Sorted array: {sorted_arr}")

start = datetime.now()
for i in range(200000):
    quicksort(arr)
end = datetime.now()
print(end - start)



def timsort(arr):
    min_run = 32
    n = len(arr)

    def insertion_sort(arr, left, right):
        for i in range(left + 1, right + 1):
            element = arr[i]
            j = i - 1
            while j >= left and arr[j] > element:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = element

    def merge(left, right):
        if not left:
            return right
        if not right:
            return left
        if left[0] < right[0]:
            return [left[0]] + merge(left[1:], right)
        return [right[0]] + merge(left, right[1:])

    # Step 1: Sort small chunks with insertion sort
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)

    # Step 2: Merge sorted chunks
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            # Merge the two halves
            merged_array = merge(arr[left:mid + 1], arr[mid + 1:right + 1])
            arr[left:left + len(merged_array)] = merged_array

        size *= 2

    return arr


# Example usage
arr = random_numbers
sorted_arr = timsort(arr)
print(f"Sorted array: {sorted_arr}")



start1 = datetime.now()
for i in range(200000):
    timsort(arr)
end1 = datetime.now()
print(end1 - start1)