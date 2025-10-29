from excel_utils import load_excel
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = load_excel()

# We are to create a grouped bar graph
# The categories are in the columns and the bar series are the rows

df.set_index("Group", inplace=True)
bar_series = df.index
categories = [col for col in df.columns if col.endswith("hr")]
width = 0.15
x = np.arange(len(categories))

# Create the bar plot
for i, series in enumerate(bar_series):
    plt.bar(x + i*width, df.loc[series], width=width, label=series)

plt.xticks(x + width*(len(bar_series)/2 - 0.5), categories)
plt.xlabel("Timepoint")
plt.ylabel("Value")
plt.legend(title="Treatment")
plt.show()
