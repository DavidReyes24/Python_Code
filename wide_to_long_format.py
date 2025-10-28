"""
Example code showing how to transform excel data in a "wide format" into the "long format" for creating grouped bar plots. 
The data example has 3 timepoints with 5 groups in each.
"""
from excel_utils import load_excel
import pandas as pd
import matplotlib.pyplot as plt

df = load_excel()
print(df.head())    # It is in wide format

df_long = df.melt(
    id_vars="Group",     # Column to keep as identifier
    var_name="Category", # Name of the new column for categories
    value_name="Value",  # Name of the new column holding values
)

print(df_long)  # It is now in long format