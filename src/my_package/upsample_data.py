import numpy as np


def upsample_y_and_x(heights, decimal_places=6):
    upsample_factor = 2

    # Calculate the new dimensions
    new_height = heights.shape[0] * upsample_factor
    new_width = heights.shape[1] * upsample_factor

    # Create a new empty array with the increased resolution
    upsampled_data = np.empty((new_height, new_width))

    # Interpolate in the Y direction
    for i in range(new_height):
        original_row = i // upsample_factor
        next_row = min(original_row + 1, heights.shape[0] - 1)
        alpha_y = i % upsample_factor / upsample_factor

        # Interpolate between two neighboring rows without rounding
        interpolated_row = (1 - alpha_y) * heights[original_row] + alpha_y * heights[next_row]

        # Interpolate in the X direction
        for j in range(new_width):
            original_col = j // upsample_factor
            next_col = min(original_col + 1, heights.shape[1] - 1)
            alpha_x = j % upsample_factor / upsample_factor

            # Interpolate between two neighboring columns without rounding
            interpolated_value = (1 - alpha_x) * interpolated_row[original_col] + alpha_x * interpolated_row[next_col]

            upsampled_data[i, j] = interpolated_value

    # Define the CSV file name
    csv_filename = "upsampled_data.csv"

    # Generate the format string for the desired decimal places
    fmt = f"%0.{decimal_places}f"

    # Save the upsampled data to a CSV file with the specified decimal places
    np.savetxt(csv_filename, upsampled_data, delimiter=",", fmt=fmt)

    print(f"Upsampled data saved to {csv_filename}")
