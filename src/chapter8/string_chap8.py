import os
import re


def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2)-1
    while j > 0:
        if word1[i] != word2[j]:
            return False
        i += 1
        j -=1
    return True

assert is_reverse( "sprint", "tnirps")==True


def find_first (pattern):
    for line in open ('pg345.txt', encoding='utf-8', errors='replace'):
        result = re.search (pattern, line)
        if result is not None:
            return result


def is_special_line (line):
    return line.startswith ('*** ')


def delete_file (file_path):
    if os.path.exists (file_path):
        # Delete the file
        os.remove (file_path)
        print (f"{file_path} has been deleted.")


def count_matches (pattern):
    count = 0
    for line in open ('pg345.txt', encoding='utf-8', errors='replace'):
        result = re.search (pattern, line)
        if result is not None:
            count += 1
    return count


def start ():
    delete_file ('pg345_cleaned.txt')
    delete_file ('pg345_replaced.txt')
    reader = open ('pg345.txt', encoding='utf-8', errors='replace')
    writer = open ('pg345_cleaned.txt', 'w', encoding='utf-8')

    for line in reader:
        if is_special_line (line):
            break
        writer.write (line)

    total = 0
    for line in open ('pg345_cleaned.txt', encoding='utf-8'):
        total += line.count ('Jonathan')
        line = line.strip ()
        if len (line) > 0:
            print (line)
        if line.endswith ('Stoker'):
            break
    writer = open ('pg345_replaced.txt', 'w', encoding='utf-8')

    for line in open ('pg345_cleaned.txt', encoding='utf-8'):
        line = line.replace ('Jonathan', 'Thomas')
        writer.write (line)

    result = find_first (r'Bram|Stokers|Jonathan')
    print (result)
    print (count_matches (r'Dracula|Stokers|Jonathan'))
    result = find_first ('^The')
    print (result)
    result = find_first ('Harker$')
    print (result)

    pattern = 'cent(er|re)'
    result = find_first (pattern)
    print (result)

    pattern = 'colou?r'
    result = find_first (pattern)
    line = result.string
    print (line)


# Regular expression pattern to match a 10-digit phone number with hyphens
pattern = re.compile (r'^\d{3}-\d{3}-\d{4}$')

# Example phone numbers to test
phone_numbers = [
    "123-456-7890",  # valid
    "123-4567-890",  # invalid
    "1234567890",  # invalid
    "123-456-78901",  # invalid
    "12-3456-7890"  # invalid
]

# Iterate through the list and check if the phone numbers match the pattern
for number in phone_numbers:
    if pattern.match (number):
        print (f"{number} is a valid phone number.")
    else:
        print (f"{number} is not a valid phone number.")

# Regular expression pattern to match a street address with a number and street name followed by ST or AVE
pattern = re.compile (r'^\d+\s+\w+(\s+\w+)*\s+(ST|AVE)$')

# Example street addresses to test
addresses = [
    "123 Main ST",  # valid
    "456 Elm AVE",  # valid
    "789 Oak Street",  # invalid (Street instead of ST)
    "1010 Maple AV",  # invalid (AV instead of AVE)
    "1111 Pine Blvd",  # invalid (Blvd instead of ST or AVE)
    "2222 Birch AVE ",  # invalid (trailing space)
]

# Iterate through the list and check if the addresses match the pattern
for address in addresses:
    if pattern.match (address):
        print (f"'{address}' is a valid address.")
    else:
        print (f"'{address}' is not a valid address.")

# Regular expression pattern to match a full name with a title and capitalized names, possibly with hyphens
pattern = re.compile (
    r'^(Mr|Mrs|Ms|Dr|Prof)\.?\s+[A-Z][a-zA-Z]*(?:-[A-Z][a-zA-Z]*)*(?:\s+[A-Z][a-zA-Z]*(?:-[A-Z][a-zA-Z]*)*)*$')

# Example names to test
names = [
    "Mr. John Doe",  # valid
    "Mrs. Jane Smith",  # valid
    "Ms. Mary-Jane O'Neill",  # valid
    "Dr. Alan Turing",  # valid
    "Prof. Stephen-Hawking",  # valid
    "Mister John Doe",  # invalid (Mister is not a common title)
    "Mr John-Doe-Smith",  # valid
    "Mrs. anna bell",  # invalid (anna is not capitalized)
    "Dr. Albert-Einstein",  # valid
    "Mr. John",  # valid
]

# Iterate through the list and check if the names match the pattern
for name in names:
    if pattern.match (name):
        print (f"'{name}' is a valid name.")
    else:
        print (f"'{name}' is not a valid name.")

if __name__ == '__main__':
    start ()
