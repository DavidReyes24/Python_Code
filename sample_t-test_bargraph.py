import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import ttest_ind

# Example data
group1 = [5, 6, 7, 5, 6]
group2 = [8, 9, 7, 10, 9]

# Calculate means and standard errors
means = [np.mean(group1), np.mean(group2)]
sems = [np.std(group1, ddof=1)/np.sqrt(len(group1)),
        np.std(group2, ddof=1)/np.sqrt(len(group2))]

# Create bar plot
fig, ax = plt.subplots()
bars = ax.bar([0, 1], means, yerr=sems, capsize=5, color=['skyblue', 'salmon'])

# Perform t-test
t_stat, p_val = ttest_ind(group1, group2)

# Decide significance marker
if p_val < 0.001:
    sig = '***'
elif p_val < 0.01:
    sig = '**'
elif p_val < 0.05:
    sig = '*'
else:
    sig = 'ns'  # not significant

# Add significance annotation
# Coordinates for the line and text
x1, x2 = 0, 1
y, h, col = max(means) + max(sems) + 0.5, 0.2, 'k'  # y: height of line, h: line thickness

# Draw line
ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
# Add text
ax.text((x1+x2)/2, y+h, sig, ha='center', va='bottom', color=col, fontsize=12)

# Labels
ax.set_xticks([0, 1])
ax.set_xticklabels(['Group 1', 'Group 2'])
ax.set_ylabel('Value')

plt.show()
