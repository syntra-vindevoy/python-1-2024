import time

import pandas as pd

# Timer starts before writing to parquet
start_time = time.time()

df = pd.read_parquet("dummy_data.parquet")

# Timer ends after writing to parquet
end_time = time.time()

# Print the time taken
print(f"Reading to parquet file took {end_time - start_time:.2f} seconds.")

print(df.info())
print(df.head())
