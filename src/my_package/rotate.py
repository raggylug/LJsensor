# rotate_plot.py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
from scipy.interpolate import griddata


def rotate_z(x, y, theta):
    """
    Rotate points around the Z axis.
    """
    theta_rad = math.radians(theta)
    x_rot = x * np.cos(theta_rad) - y * np.sin(theta_rad)
    y_rot = x * np.sin(theta_rad) + y * np.cos(theta_rad)
    return x_rot, y_rot


def plot_3d_rotate(height_data, theta, y_range=(8000, 15000), downsample_factor=1):
    """
    Plot the 3D data after rotating it around the Z-axis.
    Selects a specific range of y values and downsamples the data for efficiency.
    """
    # Select the specific range of y values and downsample
    height_data = height_data[y_range[0]:y_range[1]:downsample_factor, ::downsample_factor]

    y, x = height_data.shape
    X, Y = np.meshgrid(np.arange(x), np.arange(*y_range, downsample_factor))
    Z = height_data

    # Flatten the arrays for rotation
    X_flat, Y_flat = X.flatten(), Y.flatten()
    Z_flat = Z.flatten()

    # Rotate around the Z-axis
    X_rot, Y_rot = rotate_z(X_flat, Y_flat, theta)

    # Determine the bounds of the new grid
    x_min, x_max = np.min(X_rot), np.max(X_rot)
    y_min, y_max = np.min(Y_rot), np.max(Y_rot)

    # Define the new grid
    grid_x, grid_y = np.mgrid[x_min:x_max:complex(0, x), y_min:y_max:complex(0, y)]

    # Interpolate onto the new grid
    if len(X_rot) == len(Y_rot) == len(Z_flat):
        grid_z = griddata((X_rot, Y_rot), Z_flat, (grid_x, grid_y), method='nearest')

        # Create a figure for 3D plotting
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(X_rot, Y_rot, Z_flat, c=Z_flat, cmap='viridis', marker='.')
        ax.set_xlabel('X Axis')
        ax.set_ylabel('Y Axis')
        ax.set_zlabel('Z Axis (Height)')
        plt.title(f"Rotated 3D Plot by {theta} degrees")
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()

        return grid_z
    else:
        raise ValueError("Mismatch in array lengths after rotation")
