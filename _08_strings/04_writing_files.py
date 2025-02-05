# Open files specifying the encoding to handle non-ASCII characters
reader = open("pg345.txt", encoding="utf-8")


# Define a function to identify special lines
def is_special_line(line):
    return line.startswith("*** ")


# Print special lines
for line in reader:
    if is_special_line(line):
        print(line.strip())

# Reopen the reader to restart from the top and prepare writer
reader = open("pg345.txt", encoding="utf-8")
writer = open("pg345_cleaned.txt", "w", encoding="utf-8")

# Skip lines until the first special line
for line in reader:
    if is_special_line(line):
        break

# Write lines between the two special lines to the cleaned file
for line in reader:
    if is_special_line(line):
        break
    writer.write(line)


for line in open("pg345_cleaned.txt", encoding="utf-8"):
    line = line.strip()
    if len(line) > 0:
        print(line)
    if line.endswith("Stoker"):
        break


# Close the reader and writer
reader.close()
writer.close()

