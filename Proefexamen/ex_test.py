# Read countries info into a dict for fast lookups
with open("landen.txt", "r") as f:
    dict_countries = {}
    for line in f:
        parts = line.strip().split(',')
        if len(parts) >= 3:
            code, name, threshold = parts[0], parts[1], float(parts[2])
            dict_countries[code] = (name, threshold)

# Compute sums directly as we process the usage file
country_sums = {}

with open("verbruik.txt", "r") as f:
    for line in f:
        usage_row = line.strip().split(',')
        if len(usage_row) < 4:
            continue

        code = usage_row[0]
        date = usage_row[1]
        try:
            usage_original = float(usage_row[3])
        except ValueError:
            continue

        if date != '2024':
            continue

        if code in dict_countries:
            country_name, threshold = dict_countries[code]
            usage_adjusted = max(usage_original, threshold)
        else:
            country_name = "Unknown"
            usage_adjusted = usage_original

        if code not in country_sums:
            # country_name, sum_adj, sum_orig
            country_sums[code] = [country_name, 0.0, 0.0]
        country_sums[code][1] += usage_adjusted
        country_sums[code][2] += usage_original

# Sort and write results
sums_list = sorted(
    ([code, info[0], info[1], info[2]] for code, info in country_sums.items()),
    key=lambda x: x[1]  # Sort by country name
)

with open("test.txt", "w") as outfile:
    for row in sums_list:
        outfile.write(f"{row[0]},{row[1]},{row[2]},{row[2] - row[3]}\n")
        print(f"{row[0]},{row[1]},{row[2]},{row[2] - row[3]}")