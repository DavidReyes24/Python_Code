from excel_utils import load_excel
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

categories = ['A', 'B', 'C']          # categories on x-axis
trial1 = [5, 7, 4]                    # values for trial 1
trial2 = [6, 8, 5]                    # values for trial 2
trial3 = [7, 6, 6]                    # values for trial 3

x = np.arange(len(categories))  # [0,1,2] positions for categories
width = 0.25                    # width of each bar

plt.bar(x - width, trial1, width, label='Trial 1')
plt.bar(x, trial2, width, label='Trial 2')
plt.bar(x + width, trial3, width, label='Trial 3')

plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Grouped Bar Chart Example')
plt.xticks(x, categories)  # set x ticks to category labels
plt.legend()
plt.show()

