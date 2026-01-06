import math

def calculate_displacement(u, a, t):
    """
    Author: Kijun Lee, Date: 30/12/2025
    Purpose: Calculate displacement using s = ut + 0.5at^2
    Inputs: 
        u - initial velocity (m/s)
        a - acceleration (m/s^2)
        t - time (s)
    Outputs: 
        s - displacement (m)
    """
    s = u * t + 0.5 * a * t ** 2
    return s

# --- Main Program ---
# CO22 requires code to be testable [cite: 112]
print("--- SUVAT Solver ---")
try:
    u_in = float(input("Enter initial velocity (u): "))
    a_in = float(input("Enter acceleration (a): "))
    t_in = float(input("Enter time (t): "))
    #input functions to get user inputs for u, a, t
    #float functions to convert string inputs to float numbers

    displacement = calculate_displacement(u_in, a_in, t_in)
    print(f"The displacement is: {displacement} meters")
    #f-string to format the output
except ValueError:
    print("Error: Please enter numbers only!")
# try-except block to handle invalid inputs
