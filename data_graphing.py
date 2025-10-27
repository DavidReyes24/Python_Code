from excel_utils import load_excel
import pandas as pd
import matplotlib.pyplot as plt

df = load_excel()
print(df.head())
print(df.columns)
print(df.describe())

plt.scatter(df["Weight_g"], df["Protein_Level"], marker="s", c="#075C4B")
plt.xlabel("Weight (g)")
plt.ylabel("Protein_level (arbitrary)")
plt.title("Protein level vs Weight")
plt.show()
