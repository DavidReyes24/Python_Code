import matplotlib.pyplot as plt

fig, axs = plt.subplots(nrows=2, ncols=3, constrained_layout=True)
# Data
x_data = [
    [1, 2, 3, 4],
    [3, 6, 9, 12]
]

y_data = [
    [10, 20, 30, 40],
    [40, 30, 20, 10],
    [30, 40, 10, 20]
]

for i in range(2):
    for j in range(3):
        axs[i,j].plot(x_data[i], y_data[j])
        axs[i,j].set_title(f"Plot {i},{j}")
        axs[i,j].set_xlabel("X-axis")
        axs[i,j].set_ylabel("Y-axis")
plt.show()