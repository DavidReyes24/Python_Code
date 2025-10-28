from excel_utils import load_excel

"""
This function is used to transform "wide format" excel data to "long format" excel data. This is useful for when using plt.bar()
to create grouped bar graphs. 
"""
def wide_to_long_excel():
    df_wide = load_excel() # The imported dataframe is in the "wide format"
    print("Here is the wide format head")
    print(df_wide.head())

    df_long = df_wide.melt(
        id_vars="Group",        # Column to keep as identifier
        var_name="Categories",   # Name of the new column for categories
        value_name="Value",      # Name of the new column for holding values
    )

    return df_long

    print("Here is the head of the excel data now in long format")
    print(df_long.head())
