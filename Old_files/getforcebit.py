#
# import struct
#
#
# def read_and_parse_file(filename):
#     """Read the file and convert lines into lists of words."""
#     with open(filename, "r") as f:
#         return [line.split() for line in f if line.strip()]
#
#
# def convert_and_process_list(word_lists):
#     """Convert and process each list of words efficiently."""
#     queryset = [
#         [chr(int(sublist[0][:2], 16)) + str(int(sublist[0][2:], 16)).zfill(5)]
#         for sublist in word_lists if sublist
#     ]
#     return queryset
#
#
# if __name__ == "__main__":
#     words_list = read_and_parse_file("for.dat")
#     converted_list = convert_and_process_list(words_list)
#     for sublist in converted_list:
#         print(sublist)
#
import struct


def read_and_parse_file(filename):
    """Read the file and convert lines into lists of words."""
    with open(filename, "r") as f:
        return [line.split() for line in f if line.strip()]


def convert_and_process_list(word_lists):
    """
    Convert and process each list of words efficiently.

    Args:
        word_lists (list of list): The original list containing sublists with multiple items.

    Returns:
        list of list: Each sublist contains the processed first item and the second item.
    """
    queryset = []
    for sublist in word_lists:
        if len(sublist) >= 2:
            # Process the first item
            first_item_processed = chr(int(sublist[0][:2], 16)) + str(int(sublist[0][2:], 16)).zfill(5)
            # Take the second item as is
            second_item = sublist[1]
            # Append the processed items as a new sublist
            queryset.append([first_item_processed, second_item])
    return queryset


if __name__ == "__main__":
    words_list = read_and_parse_file("../python-1-2024-25-PLC-Forceringen/Groepswerk/for.dat")

    # Convert and process the list
    converted_list = convert_and_process_list(words_list)

    # Print the converted list
    for sublist in converted_list:
        print(sublist)

#

#
#
# if __name__ == "__main__":
#     words_list = read_and_parse_file("for.dat")
#     print(words_list)
#     converted_list = convert_and_process_list(words_list)
#     # common_elements = convert_variable_list(converted_list)
#     for sublist in converted_list:
#         print(sublist)
#     # for sublist in common_elements:
#     #     print(sublist)