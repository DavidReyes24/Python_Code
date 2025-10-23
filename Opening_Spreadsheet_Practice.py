import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Open a file dialog
Tk().withdraw()     # Hide the main Tkinter window
file_path = askopenfilename(filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])

# Load CSV into a pandas DataFrame
df = pd.read_csv(file_path)

# Show the first 5 rows
print(df.head())
print()
# Additional Useful Checks
print(df.shape)     # rows and columns
print()
print(df.columns)   # column names
print()
print(df.info())    # data types and non null values
print()
print(df.describe())# summary stats for numeric columns
print()

# Get the "Weight_g" column
weights = df["Weight_g"]
print(weights)
print()

# Getting the weights as a plain list
weights_list = df["Weight_g"].tolist()
print(weights_list)     #[20.5, 21.0, 19.8]
mean_weights = sum(weights_list)/len(weights_list)
print(f"Weights Mean: {mean_weights} g")


