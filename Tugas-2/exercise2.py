import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

mean = 0.8
std_dev = 0.1
x_min = 0.5
x_max = 1.1

x = np.linspace(x_min, x_max, 1000)

y = norm.pdf(x, mean, std_dev)

plt.plot(x, y, label='Normal Distribution')

plt.axvline(mean, color='red', linestyle='dashed', linewidth=1, label='Mean')
plt.axvline(mean + std_dev, color='blue', linestyle='dashed', linewidth=1, label='Mean + 1 Standard Deviation')
plt.axvline(mean - std_dev, color='blue', linestyle='dashed', linewidth=1, label='Mean - 1 Standard Deviation')
plt.axvline(mean + 2*std_dev, color='green', linestyle='dashed', linewidth=1, label='Mean + 2 Standard Deviations')
plt.axvline(mean - 2*std_dev, color='green', linestyle='dashed', linewidth=1, label='Mean - 2 Standard Deviations')

plt.fill_between(x, y, where=(x >= mean - std_dev) & (x <= mean + std_dev), color='lightblue', alpha=0.3)
plt.fill_between(x, y, where=(x >= mean - 2*std_dev) & (x <= mean + 2*std_dev), color='lightgreen', alpha=0.3)

plt.xlabel('time (second)')
plt.ylabel('Probability Density')
plt.title('Normal Distribution with Empirical Rule')

plt.legend()

plt.show()
