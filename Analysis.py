import numpy as np
import matplotlib.pyplot as plt

# Define the true pH value and the measurement error
pH_true = 7.0
pH_error = 0.1

# Simulate the pH meter readings
n_measurements = 100
pH_measurements = np.random.normal(pH_true, pH_error, n_measurements)

# Plot the histogram of the pH measurements
plt.hist(pH_measurements, bins=20)
plt.xlabel('pH')
plt.ylabel('Counts')
plt.title('pH Measurement Histogram')
plt.show()

# Calculate the mean and standard deviation of the pH measurements
mean_pH = np.mean(pH_measurements)
std_pH = np.std(pH_measurements)

# Print the results
print(f"Mean pH: {mean_pH:.2f}")
print(f"Standard deviation: {std_pH:.2f}")
