import time

import numpy as np
import pandas as pd

# Create 26 column names A to Z
columns = [chr(i) for i in range(65, 91)]  # ASCII codes for A-Z

# Generate 1 million rows of random dummy data
rows = 10 ** 6
data = np.random.random(size=(rows, len(columns)))

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Timer starts before writing to parquet
start_time = time.time()

# Write DataFrame to a Parquet file
df.to_parquet("dummy_data.parquet", engine="fastparquet", index=False)

# Timer ends after writing to parquet
end_time = time.time()

# Print the time taken
print(f"Writing to parquet file took {end_time - start_time:.2f} seconds.")
