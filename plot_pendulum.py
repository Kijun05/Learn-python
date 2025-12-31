import numpy as np
import matplotlib.pyplot as plt

"""
Author: Kijun
Date: 31/12/2025
Purpose: Visualize pendulum period distribution for Day 2.
Inputs: Cleaned NumPy array
Outputs: A saved .png plot and a pop-up window
"""

# 1. Prepare Data
data = np.array([2.01, 2.12, 1.98, 2.05, 2.03, 2.10, 2.08, 1.99, 2.02])

# 2. Create the Plot
plt.figure(figsize=(8, 5))
plt.hist(data, bins=5, color='skyblue', edgecolor='black')

# 3. Labeling (Vital for CO22 Lab standards)
plt.title("Distribution of Pendulum Period Measurements")
plt.xlabel("Period (seconds)")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 4. Show and Save
plt.savefig("pendulum_plot.png")
print("Plot saved as pendulum_plot.png")
plt.show()