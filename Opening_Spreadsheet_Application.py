import pandas as pd
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

while True:
    file_name = filedialog.askopenfilename(
        title="Select an Excel file",
        filetypes=[("Excel Files", "*.xls *.xlsx"), ("All files", "*.*")])


    try:
        if not file_name: 
            raise FileNotFoundError("File not selected")
        if not (file_name.endswith(".xls") or (file_name.endswith(".xlsx"))):
            raise ValueError("Not an Excel file")
        
        df = pd.read_excel(file_name)
        print(f"Excel file selected: {file_name}")
        root.destroy()
        break

    except FileNotFoundError as e:
        print(f"Error Detected: {e}")

    except ValueError as e:
        print(f"Please Try Again: {e}")

print(df.head(11))
print(df.describe())
print()

df_weight_sorted = df.sort_values(by="Weight_g", ascending=True)
print(df_weight_sorted.head(11))

print("Unsorted [5][Weight_g]", df.iloc[5]["Weight_g"])
print("Sorted [5][Weight_g]", df_weight_sorted.iloc[5]["Weight_g"])

