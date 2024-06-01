import numpy as np

# Task 1

# Create a 3x3 NumPy array filled with random numbers
random_array = np.random.random((3, 3))
print("Random Array:\n", random_array)

# Compute the mean
mean_value = np.mean(random_array)
print("Mean:", mean_value)

# Compute the median
median_value = np.median(random_array)
print("Median:", median_value)

# Compute the standard deviation
std_deviation = np.std(random_array)
print("Standard Deviation:", std_deviation)
