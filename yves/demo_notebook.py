#%%
import os
from pathlib import Path

import pandas as pd
import numpy as np

#%%
current_path = os.getcwd()
print(current_path)
df = pd.read_csv(os.path.join(current_path, "words.txt"))

#%%
print(df.info())





