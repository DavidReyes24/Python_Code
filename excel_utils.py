# excel_utils.py
# Using Tkinter to read an Excel Spreadsheet into a pandas dataframe

import pandas as pd
from tkinter import Tk, filedialog

# To use: from excel_utils import load_excel
def load_excel():
    """
    Opens a file dialog for the user to select an Excel file.
    Returns a pandas Dataframe.
    Repeats until a valid Excel file is selected.
    """
    root = Tk()
    root.withdraw()

    while True:
        file_path = filedialog.askopenfilename(
            title="Please select an Excel file",
            filetypes=[("Excel Files", "*.xls *.xlsx"), ("All files", "*.*")])

        try:
            if not file_path:
                raise FileNotFoundError("File not selected")
            if not (file_path.endswith(".xls") or file_path.endswith(".xlsx")):
                raise ValueError("Excel File Not Selected")
            
            df = pd.read_excel(file_path)
            print(f"Excel file Selected: {file_path}")
            root.destroy()
            return df

        except FileNotFoundError as e:
            print(f"Error Detected: {e}")
        except ValueError as e:
            print(f"Please Try Again: {e}")

"""
This function changes a pandas dataframe loaded in a "wide format" to a "long format" making it easier to perform data
science functions on it. 
"""
def wide_to_long_df(df_wide):
        df_long = df_wide.melt(
        id_vars="Group",        # Column to keep as identifier
        var_name="Categories",  # Name of the new column for categories
        value_name="Value",     # Name of the new column for holding values
        )
        
        print("Your dataframe is now in a long format")
        print(df_long.head())
        return df_long
