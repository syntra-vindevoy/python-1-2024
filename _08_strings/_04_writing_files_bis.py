# Define a function to identify special lines
# A "special line" starts with "*** ".
def is_special_line(line):
    return line.startswith("*** ")


# Open the file for reading, specifying the encoding to handle non-ASCII characters.
with open("pg345.txt", encoding="utf-8") as reader:
    # Iterate through the file and print every special line.
    for line in reader:
        if is_special_line(line):
            print(line.strip())  # Remove trailing spaces and newline characters for cleaner output.

# Reopen the file to read again, and open another file to write processed lines.
with open("pg345.txt", encoding="utf-8") as reader, open("pg345_cleaned.txt", "w", encoding="utf-8") as writer:
    # Skip lines until the first "special line" is encountered.
    for line in reader:
        if is_special_line(line):
            break

    # Write the lines between two "special lines" to the output file.
    for line in reader:
        if is_special_line(line):
            break
        writer.write(line)  # Write the line to the cleaned file.

# Open the cleaned file to read and print its contents.
# This ensures that only non-empty lines are printed, and we stop once a line ends with "Stoker".
with open("pg345_cleaned.txt", encoding="utf-8") as cleaned_reader:
    for line in cleaned_reader:
        line = line.strip()  # Remove any leading/trailing spaces or newline characters.
        if len(line) > 0:  # Print only non-empty lines.
            print(line)
        if line.endswith("Stoker"):  # Stop printing if the line ends with "Stoker".
            break