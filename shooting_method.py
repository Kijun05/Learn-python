import numpy as np
import matplotlib.pyplot as plt

"""
Author: Kijun
Date: 02/01/2026
Purpose: Automate the search for Energy Eigenvalues using the Shooting Method.
"""

def get_last_psi(E_guess, x, V, h):
    """Runs Numerov and returns the value of the wavefunction at the end of the grid."""
    num_points = len(x)
    psi = np.zeros(num_points)
    psi[1] = 1e-5
    
    k2 = 2 * (E_guess - V)
    
    for i in range(1, num_points - 1):
        g_curr = (h**2 / 12.0) * k2[i]
        g_prev = (h**2 / 12.0) * k2[i-1]
        g_next = (h**2 / 12.0) * k2[i+1]
        
        psi[i+1] = (2 * (1 - 5 * g_curr) * psi[i] - (1 + g_prev) * psi[i-1]) / (1 + g_next)
        #TISE Numerov formula and G optimization
        
    return psi[-1], psi # Return the last value and the whole array

# Grid setup
x = np.linspace(-5, 5, 1000)
h = x[1] - x[0]
V = 0.5 * x**2

# Test two guesses(manually finding eigenvalue)
last_val_1, psi1 = get_last_psi(0.4, x, V, h)
last_val_2, psi2 = get_last_psi(0.6, x, V, h)

print(f"At E=0.4, Psi ends at: {last_val_1:.2f}")
print(f"At E=0.6, Psi ends at: {last_val_2:.2f}")

# Bisection Method to find Eigenvalue automatically

def find_eigenvalue(E_low, E_high, tolerance=1e-7):
    """Automates the search for E where the boundary condition Psi(end) = 0 is met."""
    
    # Get the signs of the tails for the initial bracket
    val_low, _ = get_last_psi(E_low, x, V, h)
    val_high, _ = get_last_psi(E_high, x, V, h)
    
    if np.sign(val_low) == np.sign(val_high):
        print("Error: Energy bracket does not contain a root (tails have the same sign).")
        return None

    while (E_high - E_low) > tolerance:
        E_mid = (E_low + E_high) / 2
        val_mid, _ = get_last_psi(E_mid, x, V, h)
        
        # Check which half of the bracket to keep
        if np.sign(val_mid) == np.sign(val_low):
            E_low = E_mid
        else:
            E_high = E_mid
            
    return (E_low + E_high) / 2

# Execute the search for the Ground State
ground_state_E = find_eigenvalue(0.4, 0.6)
print(f"Converged Ground State Energy: {ground_state_E:.6f}")

# Final Plot of the "True" Wavefunction
_, final_psi = get_last_psi(ground_state_E, x, V, h)
plt.plot(x, final_psi / np.sqrt(np.trapz(final_psi**2, x)))
plt.title(f"Ground State Wavefunction (E = {ground_state_E:.4f})")
plt.axhline(0, color='black', lw=1)
plt.show()

# For higher states(higher n), we can repeat the process
# A list of rough guesses to 'bracket' the first 3 states
# E = n + 0.5 for harmonic oscillator
# We look 0.1 below and 0.1 above the theoretical values
brackets = [(0.4, 0.6), (1.4, 1.6), (2.4, 2.6)]

print("--- Automated Eigenvalue Search ---")
for n, (low, high) in enumerate(brackets):
    E_found = find_eigenvalue(low, high)
    print(f"State n={n}: Found Energy = {E_found:.5f} (Theoretical = {n + 0.5})")