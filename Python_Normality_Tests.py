import numpy as np
from scipy import stats

# Example: generate normally distributed data
data = np.random.normal(loc=50, scale=10, size=100)

# Shapiro–Wilk test
stat, p = stats.shapiro(data)
print(f"Shapiro–Wilk Test: W={stat:.4f}, p={p:.4f}")

if p > 0.05:
    print("Fail to reject H0: Data looks normal.")
else:
    print("Reject H0: Data is not normal.")

# K-S test comparing to a normal distribution with mean and std of data
stat, p = stats.kstest(data, 'norm', args=(np.mean(data), np.std(data)))
print(f"K-S Test: stat={stat:.4f}, p={p:.4f}")

result = stats.anderson(data)
print("Anderson–Darling Statistic:", result.statistic)
print("Critical Values:", result.critical_values)
print("Significance Levels:", result.significance_level)

if result.statistic < result.critical_values[2]:  # 5% significance level
    print("Data looks normal.")
else:
    print("Data is not normal.")

# Histogram
import matplotlib.pyplot as plt

plt.figure(1)
plt.hist(data, bins=15, edgecolor='black')
plt.title("Histogram of Data")

# Q-Q Plot
import statsmodels.api as sm

sm.qqplot(data, line='s')
plt.figure(2)
plt.title("Q-Q Plot")

plt.show()
'''
START
  │
  ▼
Do you need to compare means or medians?
  │
  ▼
Test for normality (Shapiro–Wilk, Anderson–Darling, Q-Q plot)
  │
  ├── Data is normal → Use PARAMETRIC test
  │       │
  │       ▼
  │   Are the samples paired?
  │       ├── Yes → Paired t-test
  │       └── No  → Independent t-test (2 groups) / ANOVA (3+ groups)
  │
  └── Data is NOT normal → Use NON-PARAMETRIC test
          │
          ▼
      Are the samples paired?
          ├── Yes → Wilcoxon signed-rank test
          └── No  → Mann–Whitney U test (2 groups) / Kruskal–Wallis test (3+ groups)
'''
