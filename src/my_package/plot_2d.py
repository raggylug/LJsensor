import numpy as np
import matplotlib.pyplot as plt


def plot_2d_plane(X, heights, y_value):
    """
    Plot the 2D X-Z plane at a specific Y-value with the same magnification for X and Z axes.

    Parameters:
    - X: 2D array, X coordinates.
    - heights: 2D array, height data.
    - y_value: int, Y-value for the plane.

    Returns:
    None
    """
    # Find the index corresponding to the specified Y-value
    y_index = np.argmin(np.abs(np.arange(1, heights.shape[0] + 1) - y_value))

    # Extract the X and Z values for the plane
    x_values = X[y_index, :]
    z_values = heights[y_index, :]

    # Create the 2D plot
    plt.figure()
    plt.plot(x_values, z_values, label=f'Y = {y_value}')

    # Set the aspect of the plot to be equal, ensuring same magnification for X and Z axes
    plt.gca().set_aspect('equal', adjustable='box')

    # Set labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Height')
    plt.title(f'2D X-Z Plane at Y = {y_value}')

    # Display legend
    plt.legend()

    # Show the plot
    plt.show()
