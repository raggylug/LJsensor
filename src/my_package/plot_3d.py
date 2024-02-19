import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_3d_surface(x, y, heights, cmap='viridis'):
    """
    Create a 3D surface plot.

    Parameters:
    - X: 2D array, X coordinates.
    - Y: 2D array, Y coordinates.
    - heights: 2D array, height data.
    - cmap: str, colormap (default is 'viridis').

    Returns:
    None
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Create a 3D surface plot
    ax.plot_surface(x, y, heights, cmap=cmap)

    # Set the limits for X and Y axes
    ax.set_xlim(1, heights.shape[1])
    ax.set_ylim(1, heights.shape[0])

    # Set limits for Z axis with a larger range for better visualization
    z_min, z_max = np.nanmin(heights), np.nanmax(heights)
    z_range = z_max - z_min
    ax.set_zlim(z_min - 0.2 * z_range, z_max + 0.2 * z_range)

    # Adjust scaling for X, Y, and Z axes separately
    plt.gca().set_aspect('equal', adjustable='box')

    # Set labels with smaller font size
    ax.set_xlabel('X-axis', fontsize=8)
    ax.set_ylabel('Y-axis', fontsize=8)
    ax.set_zlabel('Height', fontsize=8)

    # Set tick label font size for all three axes
    ax.tick_params(axis='x', labelsize=8)
    ax.tick_params(axis='y', labelsize=8)
    ax.tick_params(axis='z', labelsize=8)

    # Show the plot
    plt.show()