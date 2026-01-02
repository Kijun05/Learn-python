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

# 5. Initialize the Wavefunction Array with Zeros
# We create an array of the same length as our x-axis
psi = np.zeros(len(x))

# 6. Set Boundary Conditions (Mandatory for Numerov)
# At the very edge of our 'box', the particle cannot exist
psi[0] = 0.0
psi[1] = 1e-5 # A tiny 'seed' value to start the integration

print(f"Wavefunction array initialized. Total points: {len(psi)}")

# 7. Define the Physics Constants (Standardized for CO22)
E = 0.5  # Initial guess for the ground state energy
k_squared = 2 * (E - V)  # This is the 'f(x)' in the Numerov formula

# 8. The Numerov Loop
# We start at index 1 because we need i and i-1 to find i+1
# Psi formula from CO22 Lab script
# G optimisation is adapted
for i in range(1, num_points - 1):
    # Pre-calculate the 'g' factors to keep the formula clean
    g_curr = (h**2 / 12.0) * k_squared[i]
    g_prev = (h**2 / 12.0) * k_squared[i-1]
    g_next = (h**2 / 12.0) * k_squared[i+1]
    
    # The standard Numerov Step
    term1 = 2 * (1 - 5 * g_curr) * psi[i]
    term2 = (1 + g_prev) * psi[i-1]
    denominator = 1 + g_next
    
    psi[i+1] = (term1 - term2) / denominator
    """
    # Simple Finite Difference (Non-Optimized)
    psi[i+1] = (2 - h**2 * k_squared[i]) * psi[i] - psi[i-1]
    """

#normalising the wavefunction
# 1. Calculate the probability density
prob_density = psi**2

# 2. Integrate using the Trapezoid Rule (Standard NumPy method)
total_area = np.trapz(prob_density, x)

# 3. Calculate the Normalization Constant (N)
# Since Area * (1/N^2) = 1, then N = sqrt(Area)
norm_constant = np.sqrt(total_area)

# 4. Normalize the wavefunction
psi_norm = psi / norm_constant

# Verify: The area of the normalized wavefunction should now be 1.0
print(f"Original Area: {total_area:.6f}")
print(f"New Area (Normalized): {np.trapz(psi_norm**2, x):.1f}")

# 9. Plot the Result
plt.plot(x, psi_norm, label=f"Wavefunction (E={E})", color='blue')
plt.axhline(0, color='black', linestyle='--') # Show the x-axis
plt.title("Wavefunction grown via Numerov Method")
plt.xlabel("Position (x)")
plt.ylabel("Psi(x)")
plt.legend()
plt.show()

