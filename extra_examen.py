# python
from datetime import datetime

start = datetime.now()

# Read and preprocess country data (convert threshold to float upfront)
with open("python1-2024-25-tom/examen_2/landen.txt", "r") as f:
    dict_countries = {}
    for line in f:
        parts = line.strip().split(',')
        if len(parts) < 3:
            continue
        code = parts[0]
        # Store the country name and pre-converted threshold
        dict_countries[code] = (parts[1], float(parts[2]))

# Process usage file in one pass and compute sums on the fly
country_sums = {}  # code -> [country_name, sum_adjusted, sum_original]

with open("python1-2024-25-tom/examen_2/verbruik.txt", "r") as f:
    for line in f:
        parts = line.strip().split(',')
        if len(parts) < 4:
            continue

        code, date_str, usage_val = parts[0], parts[1], parts[3]
        if date_str != "2024":
            continue

        try:
            usage_original = float(usage_val)
        except ValueError:
            continue

        if code in dict_countries:
            country_name, threshold = dict_countries[code]
            usage_adjusted = usage_original if usage_original >= threshold else threshold
        else:
            country_name = "Unknown"
            usage_adjusted = usage_original

        if code not in country_sums:
            country_sums[code] = [country_name, 0.0, 0.0]
        country_sums[code][1] += usage_adjusted
        country_sums[code][2] += usage_original

# Create sorted list on country name and format the output
sums_list = sorted(
    ((code, data[0], data[1], data[2]) for code, data in country_sums.items()),
    key=lambda x: x[1]
)

with open("test.txt", "w") as outfile:
    outfile.write("\n".join(
        f"{code},{country},{adj},{adj - orig}"
        for code, country, adj, orig in sums_list
    ))

end = datetime.now()
print(f"Time taken: {(end - start).total_seconds()} seconds")
