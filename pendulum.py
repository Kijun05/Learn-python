"""
Author: Kijun
Date: 31/12/2025
Purpose: Filter experimental noise and calculate the mean period.
Inputs: raw_data (list of floats/strings)
Outputs: mean_period (float)
"""
# Experimental measurements (seconds)
# -99.0 represents a sensor timeout, "ERROR" is a manual entry mistake
raw_data = [2.01, 2.12, -99.0, 1.98, "ERROR", 2.05, 2.03]
clean_data = []
for entry in raw_data:
    if isinstance(entry, (int, float)) and entry > 0:
        # isinstance check to ensure entry is a number(int or float)
        clean_data.append(entry)
    else:
        print(f"Skipping invalid data point: {entry}")
        # so the user konows which data points were invalid and skipped
if len(clean_data) > 0:
# legnth check to avoid division by zero
    mean_period = sum(clean_data) / len(clean_data)
    print(f"Mean Period: {mean_period:.3f} seconds")
    # .3f to format the output to 3 decimal places

"""
# Using numPy for efficiency
import numpy as np  # 'np' is the universal shorthand for numpy

# We convert our list into a NumPy Array
# (Note: NumPy works best when all data starts as numbers)
data = np.array([2.01, 2.12, -99.0, 1.98, 2.05, 2.03])
double_data = data * 2  # NumPy allows this kind of operation directly on arrays

#Alternative method using NumPy
import numpy as np
data = np.array([2.0, 2.1, 1.9])
# Clean and double in one line!
clean_double = data[data > 0] * 2

# THE POWER OF NUMPY: One-line filtering
# This says: "Keep only the numbers in 'data' that are greater than 0"
clean_data = double_data[data > 0]

# High-speed calculations
mean_val = np.mean(clean_data)
std_dev = np.std(clean_data)

print(f"Cleaned Data: {clean_data}")
print(f"Mean Period: {mean_val:.3f} s")
print(f"Standard Deviation: {std_dev:.3f} s")
"""