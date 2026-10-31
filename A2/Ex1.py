# Read in a  file from a URL and save a local CSV file with the first 10 rows.
# 

import ssl
import pandas as pd
import numpy as np
import pyarrow

filename = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

# Temporary fix (for SSL certificate verification issues)
ssl._create_default_https_context = ssl._create_unverified_context
df = pd.read_csv(filename, engine='python')

out_file = "sales_data_test.csv"
df.head(10).to_csv(out_file, index=False)
print(f"Saved first 10 rows to {out_file}")