import numpy as np
import matplotlib.pyplot as plt

"""
Author: Kijun
Date: 01/01/2026
Purpose: Initialize the numerical grid for Numerov integration.
Inputs: x_start, x_end, num_points
Outputs: x_array, step_size (h)
"""

# 1. Define the physical boundaries
x_start = -5.0
x_end = 5.0
num_points = 1000  # More points = higher accuracy

# 2. Create the grid
# linspace creates 'num_points' equally spaced numbers
x = np.linspace(x_start, x_end, num_points)

# 3. Calculate the step size 'h' (Essential for Numerov's Formula)
h = x[1] - x[0]
#x[1] - x[0] gives the distance between the first two points

print(f"Grid initialized from {x_start} to {x_end}")
print(f"Number of points: {num_points}")
print(f"Step size (h): {h:.4f}")
#h:.4f formats h to 4 decimal places

# 4. Preview the Potential Energy V(x) for a Harmonic Oscillator
# V(x) = 0.5 * k * x^2 (Standardized Vectorized Math)
k = 1.0
V = 0.5 * k * x**2

plt.plot(x, V, label="Potential V(x)", color='black')
plt.title("Harmonic Oscillator Potential")
plt.xlabel("Position (x)")
plt.ylabel("Energy (V)")
plt.legend()
plt.show()