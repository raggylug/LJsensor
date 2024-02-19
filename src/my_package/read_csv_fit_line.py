import numpy as np
import pandas as pd
from scipy.stats import linregress

# Read the CSV file into a DataFrame
df = pd.read_csv(r'C:\Python\LJsensor\src\center_and_radius_of_circles_cylinder_9000_11000.csv')

# Define a z-score threshold for outlier detection (e.g., z_threshold = 3)
z_threshold = 2.2

# Calculate z-scores for 'x', 'y', and 'z' columns
z_scores_x = np.abs((df['x'] - df['x'].mean()) / df['x'].std())
z_scores_y = np.abs((df['y'] - df['y'].mean()) / df['y'].std())
z_scores_z = np.abs((df['z'] - df['z'].mean()) / df['z'].std())

# Filter out rows where any of the z-scores exceed the threshold
filtered_df = df[(z_scores_x <= z_threshold) & (z_scores_y <= z_threshold) & (z_scores_z <= z_threshold)]

# Extract the x, y, and z values from the filtered DataFrame
x = filtered_df['x'].values
y = filtered_df['y'].values
z = filtered_df['z'].values

# Fit a linear regression model to the filtered data for each axis using linregress
slope_x, intercept_x, r_value_x, _, _ = linregress(np.arange(len(x)), x)
slope_y, intercept_y, r_value_y, _, _ = linregress(np.arange(len(y)), y)
slope_z, intercept_z, r_value_z, _, _ = linregress(np.arange(len(z)), z)

# Calculate R-squared values for each axis
r_squared_x = r_value_x**2
r_squared_y = r_value_y**2
r_squared_z = r_value_z**2

# Calculate the overall R-squared value
overall_r_squared = (r_squared_x + r_squared_y + r_squared_z) / 3  # Average of R-squared values

# Print the linear equations for x, y, and z
x_equation = f'x = {intercept_x} + {slope_x}*t'
y_equation = f'y = {intercept_y} + {slope_y}*t'
z_equation = f'z = {intercept_z} + {slope_z}*t'

print(f'x_equation: {x_equation}')
print(f'y_equation: {y_equation}')
print(f'z_equation: {z_equation}')

# Print the overall R-squared value
print(f'Overall R-squared value: {overall_r_squared}')
