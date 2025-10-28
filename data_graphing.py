from excel_utils import load_excel
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

categories = ["Chicken", "Beef", "Pork", "Fish"]
groups = ["Class 1", "Class 2", "Class 3"]

df_vals = {
    "Class 1": [22, 18, 24, 20],
    "Class 2": [19, 16, 28, 25],
    "Class 3": [16, 23, 20, 24],
}

x = np.arange(len(categories))
n_groups = len(groups)
Width = 0.2
greys = ['#f0f0f0', '#d9d9d9', '#bdbdbd', '#969696', '#636363']
hatches = ['/', '\\', '|', '-', 'x']

for i, g in enumerate(groups):
    heights = np.array(df_vals[g])
    xpos = x + (i - (n_groups-1)/2) * Width
    bars = plt.bar(xpos, heights, Width, color=greys[i], hatch=hatches[i], label=g)

plt.xticks(x, categories, rotation=45)
plt.ylabel('Votes')
plt.title('Grouped bars with greys, hatch, and SEM')
plt.legend()
plt.grid(axis='y', alpha=0.25)
plt.tight_layout()
plt.show()