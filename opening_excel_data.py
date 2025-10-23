import pandas as pd
from tkinter import filedialog, Tk

root = Tk()
root.withdraw()

try:
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls"), ("All files", "*.*")])
    # Case 1: user clicked cancel
    if not file_path:
        raise FileNotFoundError("No file selected")
    
    # Case 2: file is not an excel file
    if not file_path.lower().endswith((".xlsx", ".xls"))
        raise ValueError("Selected file is not an Excel file")
    
    # Load the excel file into the pandas dataframe
    df = pd.read_excel(file_path)
    print("Excel file successfully selected:", file_path)
    print(df.head())
except FileNotFoundError as FNE:
    print("Error detected:", FNE)
except ValueError as VE:
    print("Error detected:", VE)
except Exception as e:
    print("An error occured:", e)
finally:
    root.destroy()