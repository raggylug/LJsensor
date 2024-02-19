import csv

import numpy as np
from src.my_package.plane_with_fitted_circle import fit_circle


def save_circle_centers_csv(x, heights, y_range):
    circle_centers = {}
    for y_value in y_range:
        result = (fit_circle(x, heights, y_value)[0], y_value, fit_circle(x, heights, y_value)[1], fit_circle(x, heights, y_value)[2], fit_circle(x, heights, y_value)[3])
        circle_centers[y_value] = result

    # Calculate the mean radius
    radii = [value[3] for value in circle_centers.values()]  # Extracting radii
    Rsquare = [value[4] for value in circle_centers.values()]
    mean_radius = np.mean(radii)
    mean_Rsquare = np.mean(Rsquare)

    # Prepare data for 3D plot
    data = np.array(list(circle_centers.values()))

    # Writing data to CSV
    with open('center_and_radius_of_circles.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['X Center', 'Y Value', 'Z Center', 'Radius', 'Rsquare'])
        for row in data:
            writer.writerow(row)
