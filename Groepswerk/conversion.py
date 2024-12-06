# Open and read the file, splitting into words
with open("for.dat", "r") as f:
    words = f.read().split("\n")
    print(words)


# Function to split strings into lists
def spilt_string(string):
    list1 = []
    for item in string:
        if item.strip():  # Check if the line is not empty
            split_items = item.split()
            list1.append(split_items)
    return list1


# Split the words into three lists
list1 = spilt_string(words)

def convert_and_split(string_list):
    processed_list = []

    for sublist in string_list:
        if sublist:  # Check if sublist is not empty
            first_part = sublist[0]
            # Split the first part into two: first two hex digits, and last six hex digits
            ascii_hex = first_part[:2]
            decimal_hex = first_part[2:]

            # Convert the ASCII hex to a character
            ascii_char = chr(int(ascii_hex, 16))

            # Convert the decimal hex to an integerS
            decimal_number = int(decimal_hex, 16)
            if len(str(decimal_number)) < 5:
                decimal_number = str(decimal_number).zfill(5)
            # Append the processed components together with the rest of the sublist
            processed_list.append([ascii_char + str(decimal_number)] + sublist[1:])

    return processed_list


# Process the list
converted_list = convert_and_split(list1)


if __name__ == "__main__":
    # Output processed list
    print(list1)
    print(converted_list)
