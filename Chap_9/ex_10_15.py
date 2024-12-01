# from datetime import timedelta
#
# t = [[1, 2], [3], [4, 5, 6]]
# total_sum = 0
#
# for i in t:
#     for j in i:
#         total_sum += j  # Add each element to the total sum
#
# print("Total sum:", total_sum)
#
# def cumsum(numbers):
#     cumulative_sum = []
#     total = 0
#     for number in numbers:
#         total += number
#         cumulative_sum.append(total)
#     return cumulative_sum
#
# # Example usage:
# z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = cumsum(z)
# print("Cumulative sum:", result)
#
#
# def middle(numbers):
#     return numbers[1:-1]
#
# t = [1, 2, 3, 4, 5]
# result1 = middle(t)
# print("middle:", result1)
#
# # Create a list of days from 23 to 3

days = list(range(22, 32)) + list(range(1, 3))


# Define the days to be removed
days_to_remove = [24, 25, 27, 28, 31, 1]

# Remove the specified days
filtered_days = [day for day in days if day not in days_to_remove]

print(f"The days that fit for me {filtered_days}")
