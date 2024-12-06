from datetime import datetime
# def number_seacher(target_number, search, counter):
#     counter += 1
#     if search > target_number:
#         search = search // 2
#         if search == target_number:
#             return search
#         elif search > target_number:
#             search = search // 2
#             search += search
#             print(f"{counter} number is higher {search}")
#             print(f"the target is {target_number}")
#             return number_seacher(target_number, search, counter)
#     elif search < target_number:
#         search = search // 2
#         if search == target_number:
#             return search
#         elif search > target_number:
#             search = search // 2
#             search += search
#             print(f"{counter} number is higher {search}")
#             print(f"the target is {target_number}")
#     elif search == target_number:
#         return search
#
# # Input and function call
# max_number = 10000
# target_number = int(input("Enter the target number (1 to 10000): "))
# final_value = number_seacher(target_number, max_number, 0)
# print("Final value:", final_value)  # Print the final value returned by the function
# import random
#
# # Generate a random number between 1 and 10000
# random_number = random.randint(1, 10000)
#
# print("Random number generated:", random_number)


start = datetime.now()

def number_searcher(target_number, search_min, search_max, counter=0):
    counter += 1
    search = (search_min + search_max) // 2

    if search == target_number:
        print(f"Target found in {counter} steps!")
        print(f"Target found in {search} steps!")
        return search
    elif search < target_number:
        print(f"Step {counter}: {search} is lower than {target_number}")
        return number_searcher(target_number, search + 1, search_max, counter)
    else:
        print(f"Step {counter}: {search} is higher than {target_number}")
        return number_searcher(target_number, search_min, search - 1, counter)


# Input and function call


end = datetime.now()

print(f"Time taken: {end - start}")

if __name__ == "__main__":
    random_number = 1
    max_number = 100000
    target_number = random_number  # int(input("Enter the target number (1 to 10000): "))
    final_value = number_searcher(target_number, 1, max_number)
    print("Final value:", final_value)
    print(max([number_searcher(i + 1, 1, max_number) for i in range(10000)]))
