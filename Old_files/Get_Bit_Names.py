import struct

def read_and_parse_file(filename):
    """Read the file and convert lines into lists of words."""
    with open(filename, "r") as f:
        return [line.split() for line in f if line.strip()]


def convert_and_process_list(word_lists):
    """Convert and process each list of words."""
    processed_list = []

    for sublist in word_lists:
        if sublist:
            # Convert the first value from hex to ascii + decimal
            first_part = sublist[0]
            ascii_hex, decimal_hex = first_part[:2], first_part[2:]
            ascii_char = chr(int(ascii_hex, 16))
            decimal_number = str(int(decimal_hex, 16)).zfill(5)
            processed_list.append([ascii_char + decimal_number] + sublist[1:])

    return processed_list


def find_common_first_elements(processed_list, words_list1):
    """Find common elements with the same first element between two lists."""
    common_keys = {sublist[0] for sublist in processed_list if sublist} & {sublist[0] for sublist in words_list1 if
                                                                           sublist}

    processed_dict = {sublist[0]: sublist[1:] for sublist in processed_list if sublist}
    words_dict = {sublist[0]: sublist[1:] for sublist in words_list1 if sublist}

    # Creating merged sublists for common first elements
    return [[key] + processed_dict[key] + words_dict[key] for key in common_keys]

def convert_variable_list(common_elements):
    """Convert and process word lists."""
    processed_list = []

    for sublist in common_elements:
        # convert the second value from IEEE 754 single-precision format to floating point
        if sublist[3] == 'R':
            int_value = int(sublist[4], 16)
            float_value = struct.unpack('!f', struct.pack('!I', int_value))[0]
            sublist[4] = str(float_value)
        # if value isn't single-precision but hex
        elif sublist[3] == 'L':
            sublist[4] = int(sublist[4], 16)
            # put it all together in one list
        processed_list.append(sublist[0:])

    return processed_list

if __name__ == "__main__":
    words_list1 = read_and_parse_file("DONP.MAP")
    words_list = read_and_parse_file("TDS.dat")
    converted_list = convert_and_process_list(words_list)
    common_elements = find_common_first_elements(words_list1, converted_list)
    common_elements = convert_variable_list(common_elements)
    for sublist in common_elements:
        print(sublist)
