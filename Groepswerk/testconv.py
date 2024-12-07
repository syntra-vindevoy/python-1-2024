import struct


def read_and_split_file(filename):
    """Read the file and split content into lists of words."""
    with open(filename, "r") as f:
        lines = f.readlines()
    return [line.split() for line in lines if line.strip()]  # Split non-empty lines


def convert_and_process_list(word_lists):
    """Convert and process word lists."""
    processed_list = []

    for sublist in word_lists:
        if sublist:
            first_part = sublist[0]
            ascii_hex, decimal_hex = first_part[:2], first_part[2:]

            ascii_char = chr(int(ascii_hex, 16))
            decimal_number = str(int(decimal_hex, 16)).zfill(5)

            if len(sublist) > 1 and sublist[1] not in {"0", "1"}:
                int_value = int(sublist[1], 16)
                float_value = struct.unpack('!f', struct.pack('!I', int_value))[0]
                sublist[1] = float_value

            processed_list.append([ascii_char + decimal_number] + sublist[1:])

    return processed_list


if __name__ == "__main__":
    words_list = read_and_split_file("TDS.dat")
    converted_list = convert_and_process_list(words_list)

    for sublist in converted_list:
        print(sublist)
