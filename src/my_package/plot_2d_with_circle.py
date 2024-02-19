import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares

def circle_equation(params, x):
    """
    Equation of a circle.

    Parameters:
    - params: array-like, parameters (h, k, r) of the circle.
    - x: array-like, input array.

    Returns:
    - array, output array.
    """
    h, k, r = params
    radicand = r**2 - (x - h)**2

    # Check for negative values under the square root and handle them
    with np.errstate(invalid='ignore'):  # Ignore warnings for invalid operations
        sqrt_result = np.sqrt(radicand)
        sqrt_result[radicand < 0] = np.nan  # Set negative radicand results to NaN

    return k - sqrt_result

def cost_function(params, x, z):
    """
    Cost function for circle fitting.

    Parameters:
    - params: array-like, parameters (h, k, r) of the circle.
    - x: array-like, input X coordinates.
    - z: array-like, input Z coordinates.

    Returns:
    - array, residuals.
    """
    return circle_equation(params, x) - z

def fit_circle(x, heights, y_value):
    """
    Fit the X-Z data at a specific Y-value to a circle.

    Parameters:
    - X: 2D array, X coordinates.
    - heights: 2D array, height data.
    - y_value: int, Y-value for the plane.

    Returns:
    - tuple, (h, k, r, r_squared), where (h, k) is the center, r is the radius, and r_squared is the R-squared value.
    """
    y_index = np.argmin(np.abs(np.arange(1, heights.shape[0] + 1) - y_value))
    x_values = x[y_index, :]
    z_values = heights[y_index, :]

    # Remove NaN and Inf values
    valid_indices = ~np.isnan(x_values) & ~np.isnan(z_values) & ~np.isinf(x_values) & ~np.isinf(z_values)
    x_values = x_values[valid_indices]
    z_values = z_values[valid_indices]

    # Initial guess for the circle parameters (h, k, r)
    initial_params = np.array([np.mean(x_values), np.mean(z_values), np.max(x_values) - np.min(x_values) / 2])

    # Define the cost function for least squares
    def cost_func(params):
        return cost_function(params, x_values, z_values)

    # Optimize the cost function using the least squares with an initial guess
    result = least_squares(cost_func, initial_params)

    # Extract the center and radius
    h, k, r = result.x

    return h, k, r

def plot_2d_plane_with_circle(x, heights, y_value):
    if len(x.shape) != 2 or len(heights.shape) != 2 or x.shape != heights.shape:
        print("Error: Input data should be 2D NumPy arrays with the same shape.")
        return

    h, k, r = fit_circle(x, heights, y_value)

    # Plot the original 2D plane
    plt.figure()
    plt.plot(x[y_value - 1, :], heights[y_value - 1, :], label=f'Original data')

    # Plot the fitted circle
    theta = np.linspace(0, 2 * np.pi, 100)
    x_circle = h + r * np.cos(theta)
    z_circle = k + r * np.sin(theta)
    plt.plot(x_circle, z_circle, label='Fitted Circle', linestyle='--')

    # Plot the center of the circle
    plt.scatter(h, k, color='red', label='Circle Center', s=5)

    # Set the aspect of the plot to be equal
    plt.gca().set_aspect('equal', adjustable='datalim')

    # Set labels and title
    plt.xlabel('X')
    plt.ylabel('Z')
    plt.title(f'Original data and Fitted circle at Y = 10000')

    # Format the tick labels to plain style and adjust font size
    plt.gca().ticklabel_format(style='plain', axis='both')
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)

    # Display legend outside the plot area
    plt.legend(loc='upper right', bbox_to_anchor=(1.0, 1.0))

    # Show the plot
    plt.show()

