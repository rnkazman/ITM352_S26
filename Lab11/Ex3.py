# Read in a CSV file and create a dataframe.
# Pivot the dataframe, aggregating sales by region, with columns defined by order_type and totals.
# Add in sub-columns showing the average sales by state and by sale type (retail or wholesale).

import pandas as pd
import numpy as np
import pyarrow
import ssl

# Temporary fix.  Don't do this in production code.
ssl._create_default_https_context = ssl._create_unverified_context

filename = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

pd.set_option('display.max_columns', None)  # Show all columns in the output
pd.set_option('display.float_format', '{:,.2f}'.format)  # Format floats to 2 decimal places

df = pd.read_csv(filename, engine='pyarrow')
df['order_date'] = pd.to_datetime(df['order_date'], format='%m/%d/%Y', errors='coerce')  # Convert order_date to datetime, coercing errors to NaT

# Coerce quantiy and unit_price to numeric, setting errors to NaN
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')
df['sales'] = df['quantity'] * df['unit_price']  # Calculate sales as quantity multiplied by unit price

pivot_table = pd.pivot_table(df,
                                 values='sales',    # What are you calculating?
                                 index='customer_state', # What are the rows?
                                 columns=['customer_type', 'order_type'], # What are the columns? 
                                 aggfunc=np.sum, # What stats are we calculating? 
                                 fill_value=0, # What value should be used for missing data?
                                 margins=True, # Add a 'Total' column and row
                                 margins_name='Total Sales')
print(pivot_table)
