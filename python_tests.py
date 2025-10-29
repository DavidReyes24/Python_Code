from excel_utils import load_excel, wide_to_long_df
import pandas as pd
import matplotlib.pyplot as plt

df = load_excel()
print(df.head())

df_long = wide_to_long_df(df)

