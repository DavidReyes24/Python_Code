from excel_utils import load_excel
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

df = load_excel()

df.set_index("Group", inplace=True)
bar_series = df.index
categories = [col for col in df.columns if col.endswith("hr")]
width = 0.15
outline_colors = ["Red", "Blue", "Green", "Orange", "Purple"]
x = np.arange(len(categories))

fig, ax = plt.subplots()

bars_all = []

# Plot each bar series and store the bar containers
for i, series in enumerate(bar_series):
    bars = ax.bar(
        x + i*width,
        df.loc[series],
        width=width,
        facecolor="white",
        edgecolor=outline_colors[i],
        linewidth=3,
        hatch="//"
    )
    bars_all.append(bars)

# Center x-ticks
ax.set_xticks(x + width*(len(bar_series)/2 - 0.5))
ax.set_xticklabels(categories)
ax.set_xlabel("Timepoint")
ax.set_ylabel("Value")

# Add uniform legend (no hatching)
legend_patches = [
    Patch(facecolor="white", edgecolor=outline_colors[i], linewidth=3, label=series)
    for i, series in enumerate(bar_series)
]
ax.legend(handles=legend_patches, title="Treatment")

# Annotate each bar with its height
for bars in bars_all:
    ax.bar_label(bars, fmt="%.1f", padding=3)  # padding shifts text above the bar

plt.tight_layout()
plt.show()
