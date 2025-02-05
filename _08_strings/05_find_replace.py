total = 0
for line in open("pg345_cleaned.txt", encoding="utf-8"):
    total += 1

print(total)


total = 0
for line in open("pg345_cleaned.txt", encoding="utf-8"):
    if "Jonathan" in line:
        total += 1

print(total)


total = 0
for line in open("pg345_cleaned.txt", encoding="utf-8"):
    total += line.count('Jonathan')

print(total)


writer = open("pg345_replaced.txt", "w", encoding="utf-8")

for line in open("pg345_cleaned.txt", encoding="utf-8"):
    line = line.replace("Jonathan", "Thomas")
    writer.write(line)


# Close the writer
writer.close()
