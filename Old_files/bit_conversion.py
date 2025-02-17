import struct
from datetime import datetime
from getforcebit import convert_and_process_list, read_and_parse_file
from Old_files.searchdatabase import search_database


def convert_variable_list(common_elements):
    """Convert and process word lists."""
    processed_list = []

    for sublist in common_elements:
        value = sublist.get("Value", "")
        type_ = sublist.get("Type")

        if type_ == 'REAL':
            int_value = int(value, 16)
            float_value = struct.unpack('!f', struct.pack('!I', int_value))[0]
            sublist["Value"] = str(float_value)
        elif type_ == 'LINT':
            sublist["Value"] = int(value, 16)
        elif type_ == 'DOUBLE':
            value_hex = value.zfill(16) if len(value) < 16 else value[:16]
            int_value = int(value_hex, 16)
            sublist["Value"] = str(int_value)

        processed_list.append(sublist)

    return processed_list


if __name__ == "__main__":
    start = datetime.now()
    words_list = read_and_parse_file("for.dat")
    item_list = convert_and_process_list(words_list)
    results = search_database(item_list)
    common_elements = convert_variable_list(results)
    end = datetime.now()

    print(f"Time taken: {(end - start).total_seconds()} seconds")
    for sublist in common_elements:
        print(sublist)
