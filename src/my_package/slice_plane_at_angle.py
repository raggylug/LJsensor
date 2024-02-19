import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import minimize
from typing import List, Tuple


def generate_u_and_v_coordinates(height_map, x0, y0, theta):
    num_rows = len(height_map)
    num_cols = len(height_map[0])

    u_coordinates = []
    v_values = []
    xy_coordinates = []

    step_size = 1.0

    x = 0
    u = 0
    theta_radians = math.radians(theta)
    cos_theta = math.cos(theta_radians)
    tan_theta = math.tan(theta_radians)

    u_max = num_cols / cos_theta

    while 0 <= u < u_max:
        x = u * cos_theta
        y = y0 + (x - x0) * tan_theta

        x_rounded = int(round(x))
        y_rounded = int(round(y))

        if x_rounded >= 3200:
            x_rounded = 3199
        if y_rounded >= 15999:
            y_rounded = 15998

        z = height_map[y_rounded][x_rounded]

        u_coordinates.append(u)
        v_values.append(z)
        xy_coordinates.append((x_rounded, y_rounded))

        u += step_size

    return np.array(u_coordinates), np.array(v_values)


def process_csv_and_generate_coordinates(csv_file_path: str, height_map, theta: float) -> List[Tuple[np.ndarray, np.ndarray]]:
    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # List to store results
    results = []

    # Process each row
    for index, row in df.iterrows():
        x0, y0 = round(row['x0']), round(row['y0'])
        u_coords, v_vals = generate_u_and_v_coordinates(height_map, x0, y0, theta)
        results.append((u_coords, v_vals))

    return results


def save_results_to_csv(results, output_file_path):
    data_dict = {}

    # Create a dictionary with separate keys for each pair's u and v values
    for i, (u_coords, v_vals) in enumerate(results):
        data_dict[f'u_{i}'] = u_coords
        data_dict[f'v_{i}'] = v_vals

    # Create a DataFrame from the dictionary
    df = pd.DataFrame.from_dict(data_dict)

    # Save the DataFrame to a CSV file
    df.to_csv(output_file_path, index=False, na_rep='NaN')

